from __future__ import annotations

import threading
import time
import uuid
from pathlib import Path
from typing import Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.job_models import GenerateRequest, JobRecord, JobStatus
from runners.personaplex_runner import run_generation

APP_NAME = "VocalForge PersonaPlex Lab Backend"
VERSION = "0.1.0"

app = FastAPI(title=APP_NAME, version=VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

jobs: Dict[str, JobRecord] = {}
job_lock = threading.Lock()


def _worker(job_id: str) -> None:
    with job_lock:
        record = jobs[job_id]
        if record.status == JobStatus.CANCELLED:
            return
        record.status = JobStatus.RUNNING
        jobs[job_id] = record

    try:
        time.sleep(0.1)
        _, output_path = run_generation(
            prompt_text=record.prompt_text,
            voice_id=record.voice_id,
            seed=record.seed,
            target_seconds=record.target_seconds,
            category=record.category,
            output_dir=record.output_dir,
            style_tags=record.style_tags,
        )
        with job_lock:
            record = jobs[job_id]
            if record.status != JobStatus.CANCELLED:
                record.status = JobStatus.COMPLETED
                record.output_file = output_path
                jobs[job_id] = record
    except Exception as exc:
        with job_lock:
            record = jobs[job_id]
            record.status = JobStatus.FAILED
            record.error = str(exc)
            jobs[job_id] = record


@app.get("/health")
def health() -> dict:
    return {"ok": True, "service": APP_NAME, "version": VERSION, "jobs": len(jobs)}


@app.get("/voices")
def voices() -> List[dict]:
    return [
        {"id": "NATF2", "name": "Natural Female 2", "notes": "maps to upstream NATF2 voice prompt"},
        {"id": "NATM1", "name": "Natural Male 1", "notes": "maps to upstream NATM1 voice prompt"},
        {"id": "VARF1", "name": "Variety Female 1", "notes": "more stylized voice bucket"},
        {"id": "VARM2", "name": "Variety Male 2", "notes": "more stylized voice bucket"},
    ]


@app.post("/generate", response_model=JobRecord)
def generate(req: GenerateRequest) -> JobRecord:
    job_id = str(uuid.uuid4())
    record = JobRecord(
        job_id=job_id,
        status=JobStatus.QUEUED,
        prompt_text=req.prompt_text,
        voice_id=req.voice_id,
        seed=req.seed,
        target_seconds=req.target_seconds,
        category=req.category,
        output_dir=req.output_dir,
        style_tags=req.style_tags,
    )
    Path(req.output_dir).mkdir(parents=True, exist_ok=True)
    with job_lock:
        jobs[job_id] = record
    thread = threading.Thread(target=_worker, args=(job_id,), daemon=True)
    thread.start()
    return record


@app.get("/jobs", response_model=List[JobRecord])
def list_jobs() -> List[JobRecord]:
    with job_lock:
        return list(jobs.values())


@app.get("/jobs/{job_id}", response_model=JobRecord)
def get_job(job_id: str) -> JobRecord:
    with job_lock:
        if job_id not in jobs:
            raise HTTPException(status_code=404, detail="Job not found")
        return jobs[job_id]


@app.post("/jobs/{job_id}/cancel", response_model=JobRecord)
def cancel_job(job_id: str) -> JobRecord:
    with job_lock:
        if job_id not in jobs:
            raise HTTPException(status_code=404, detail="Job not found")
        record = jobs[job_id]
        if record.status in {JobStatus.COMPLETED, JobStatus.FAILED}:
            return record
        record.status = JobStatus.CANCELLED
        jobs[job_id] = record
        return record

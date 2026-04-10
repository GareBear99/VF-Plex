from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class JobStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class GenerateRequest(BaseModel):
    prompt_text: str = Field(min_length=1)
    voice_id: str = Field(min_length=1)
    seed: int = Field(ge=0)
    target_seconds: float = Field(ge=0.25, le=30.0)
    category: str = Field(min_length=1)
    output_dir: str = Field(min_length=1)
    style_tags: List[str] = Field(default_factory=list)


class JobRecord(BaseModel):
    job_id: str
    status: JobStatus
    prompt_text: str
    voice_id: str
    seed: int
    target_seconds: float
    category: str
    output_dir: str
    style_tags: List[str] = Field(default_factory=list)
    output_file: Optional[str] = None
    error: Optional[str] = None

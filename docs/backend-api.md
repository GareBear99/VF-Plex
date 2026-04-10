# Backend API

## Endpoints

### `GET /health`
Returns service status.

### `GET /voices`
Returns the voice registry available to the wrapper.

### `POST /generate`
Queues a generation job.

Payload:
```json
{
  "prompt_text": "You enjoy having a good conversation.",
  "voice_id": "NATF2",
  "seed": 42424242,
  "target_seconds": 3.0,
  "category": "spoken_hooks",
  "output_dir": "./backend/outputs",
  "style_tags": ["dark", "robotic"]
}
```

### `GET /jobs`
Lists jobs.

### `GET /jobs/{job_id}`
Returns a single job.

### `POST /jobs/{job_id}/cancel`
Requests cancellation.

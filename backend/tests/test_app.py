import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    data = response.json()
    assert data['ok'] is True


def test_generate_and_poll(tmp_path):
    payload = {
        'prompt_text': 'You enjoy having a good conversation.',
        'voice_id': 'NATF2',
        'seed': 42424242,
        'target_seconds': 1.0,
        'category': 'spoken_hooks',
        'output_dir': str(tmp_path),
        'style_tags': ['dark', 'robotic'],
    }
    job = client.post('/generate', json=payload)
    assert job.status_code == 200
    job_id = job.json()['job_id']

    final = None
    for _ in range(30):
        current = client.get(f'/jobs/{job_id}')
        assert current.status_code == 200
        data = current.json()
        if data['status'] in {'completed', 'failed'}:
            final = data
            break

    assert final is not None
    assert final['status'] == 'completed'
    assert final['output_file'].endswith('.wav')

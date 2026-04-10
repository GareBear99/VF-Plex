const API = 'http://127.0.0.1:8765';

async function loadVoices() {
  const response = await fetch(`${API}/voices`);
  const voices = await response.json();
  const select = document.getElementById('voiceId');
  select.innerHTML = '';
  for (const voice of voices) {
    const option = document.createElement('option');
    option.value = voice.id;
    option.textContent = `${voice.id} — ${voice.name}`;
    select.appendChild(option);
  }
}

function renderJobs(jobs) {
  const container = document.getElementById('jobs');
  container.innerHTML = '';
  for (const job of jobs.slice().reverse()) {
    const div = document.createElement('div');
    div.className = 'job';
    div.innerHTML = `
      <strong>${job.category}</strong> · ${job.voice_id} · ${job.status}<br>
      <span class="small">${job.prompt_text}</span><br>
      <span class="small">${job.output_file || job.error || 'pending...'}</span>
    `;
    container.appendChild(div);
  }
}

async function refreshJobs() {
  const response = await fetch(`${API}/jobs`);
  const jobs = await response.json();
  renderJobs(jobs);
}

async function queueJob() {
  const payload = {
    prompt_text: document.getElementById('promptText').value,
    voice_id: document.getElementById('voiceId').value,
    seed: Number(document.getElementById('seed').value),
    target_seconds: Number(document.getElementById('targetSeconds').value),
    category: document.getElementById('category').value,
    output_dir: '../backend/outputs',
    style_tags: document.getElementById('styleTags').value.split(',').map(s => s.trim()).filter(Boolean),
  };
  document.getElementById('statusLine').textContent = 'Submitting job...';
  const response = await fetch(`${API}/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  document.getElementById('statusLine').textContent = `Queued ${data.job_id}`;
  refreshJobs();
}

document.getElementById('generateBtn').addEventListener('click', queueJob);
loadVoices().then(refreshJobs);
setInterval(refreshJobs, 1500);

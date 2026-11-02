/**
 * API service for communicating with FastAPI backend
 */

const API_BASE_URL = 'http://127.0.0.1:8000';

export async function checkBackendHealth() {
  try {
    const res = await fetch(`${API_BASE_URL}/health`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('Backend health check failed:', err.message);
    return null;
  }
}

export async function fetchModelMetrics() {
  try {
    const res = await fetch(`${API_BASE_URL}/api/model-info`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error('Failed to fetch model metrics:', err);
    throw err;
  }
}

export async function submitAssessment(formData) {
  try {
    const res = await fetch(`${API_BASE_URL}/api/predict`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });
    if (!res.ok) {
      const errDetail = await res.text();
      throw new Error(`Inference failed (HTTP ${res.status}): ${errDetail}`);
    }
    return await res.json();
  } catch (err) {
    console.error('Assessment submission error:', err);
    throw err;
  }
}

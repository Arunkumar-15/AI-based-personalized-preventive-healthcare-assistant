import json
import os

log_path = r"C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\.system_generated\logs\transcript.jsonl"

user_requests = []
if os.path.exists(log_path):
    with open(log_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            try:
                data = json.loads(line)
                if data.get('type') == 'USER_INPUT' or data.get('source') == 'USER_EXPLICIT':
                    content = data.get('content', '')
                    if content and not content.startswith('<CONTEXT_SUMMARY>') and not content.startswith('<SYSTEM_MESSAGE>'):
                        user_requests.append((idx, content.strip()))
            except Exception:
                pass

print(f"Total User Prompts Found: {len(user_requests)}")
for i, req in user_requests:
    print(f"Step {i}: {req}")

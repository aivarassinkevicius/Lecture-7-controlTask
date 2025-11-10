import requests
import json

# Test exercise routine generation
url = 'http://localhost:11434/api/generate'
data = {
    'model': 'gemma3:270m',
    'prompt': 'Create a 7-day weekly exercise routine for a 30-year-old person who wants to lose weight and can exercise 45 minutes per day. Include specific exercises for each day.',
    'stream': False
}

print('Testing exercise routine generation...')
try:
    response = requests.post(url, json=data, timeout=60)
    result = response.json()

    if 'error' in result:
        print(f'Error: {result["error"]}')
    else:
        print('Success! Generated routine:')
        print('=' * 50)
        routine = result['response']
        if len(routine) > 800:
            print(routine[:800] + '\n...[truncated]')
        else:
            print(routine)
            
except Exception as e:
    print(f'Connection error: {e}')
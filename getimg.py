import requests
import json

def generate_image(prompt, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"prompt": prompt}
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["image"]
    else:
        raise Exception(f"Error: {response.text}")

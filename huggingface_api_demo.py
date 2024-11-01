import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_token = os.getenv("HUGGINGFACE_API_TOKEN")

headers = {"Authorization": f"Bearer {api_token}"}
model_id = "gpt2"
api_url = f"https://api-inference.huggingface.co/models/{model_id}"

response = requests.post(api_url, headers=headers, json={"inputs": "Hello, world!"})
print(response.json())
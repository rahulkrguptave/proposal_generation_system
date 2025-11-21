import requests
import json
import os
from dotenv import load_dotenv

# ---------------------------------------------------------
# Load .env from project root (relative)
# ---------------------------------------------------------
# Get absolute path of the project root (one level above this file)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build path to .env file
ENV_PATH = os.path.join(BASE_DIR, ".env")

# Load .env file
load_dotenv(ENV_PATH)

# Debug print to verify key is loaded
print({"OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")})

# ---------------------------------------------------------
# GPT-4o API Call Function
# ---------------------------------------------------------
def call_gpt_4o(user_message: str):
    url = "https://api.openai.com/v1/chat/completions"

    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    data = response.json()

    raw = data["choices"][0]["message"]["content"]

    # Remove backticks and the "json" label
    clean = raw.replace("```json", "").replace("```", "").strip()

    # Convert the string into actual JSON (Python dict)
    parsed_json = json.loads(clean)

    return parsed_json
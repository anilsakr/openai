import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="prompt to send the OpenAI API")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

headers = {
    "Content-Type" : "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": f"write python script to {args.prompt}.",
    "max_tokens": 100,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=headers, json=request_data)

if response.status_code == 200:
    print(response.json()["choices"][0]["text"])
else:
    print(f"request failed: {str(response.status_code)}")

    
    
    
# python3 py-chatgpt.py "print todays date"

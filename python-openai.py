import requests



api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

headers = {
    "Content-Type" : "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "write python script for printing out todays date",
    "max_tokens": 100,
    "temperature": 0.5
}
response = requests.post(api_endpoint, headers=headers, json=request_data)

if response.status_code == 200:
    print(response.json()["choices"][0]["text"])
else:
    print(f"request failed: {str(response.status_code)} ")

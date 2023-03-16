import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="prompt to send the OpenAI API")
parser.add_argument("file_name", help="name of the file to save the py script")
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
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"request failed: {str(response.status_code)}")


# python3 py-chatgpt.py "print todays date" "print_date.py"

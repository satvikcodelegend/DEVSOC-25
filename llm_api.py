import json
import requests

API_KEY = "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"
API_URL = "https://api.openai.com/v1/chat/completions"

def read_prompts(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def fetch_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    body = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(API_URL, headers=headers, json=body)
    data = response.json()
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        return data.get("error", {}).get("message", "Unknown error")

def save_results(data, output_file):
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)

def main():
    prompts = read_prompts("prompts.txt")
    results = []
    for prompt in prompts:
        reply = fetch_response(prompt)
        results.append({"prompt": prompt, "response": reply})
    save_results(results, "responses.json")

if __name__ == "__main__":
    main()

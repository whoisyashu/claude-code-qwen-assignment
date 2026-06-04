import requests

url = "http://localhost:11434/api/generate"
prompt = input("Enter your question:\n");

payload = {
    "model": "qwen3:4b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload)

result = response.json()

print("\nModel Response:\n")
print(result["response"])
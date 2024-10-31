import requests

url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"

payload = {
	"messages": [
		{
			"role": "user",
			"content": "Hello, how is it going?"
		}
	],
	"model": "gpt-4o",
	"max_tokens": 100,
	"temperature": 0.9
}
headers = {
	"x-rapidapi-key": "f36ae49db5msh5ca484fcf24aa0ap1808c2jsnb90326d66c59",
	"x-rapidapi-host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

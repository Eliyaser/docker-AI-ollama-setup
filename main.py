import requests

# URL of the Ollama API endpoint
url = "http://localhost:11434/api/generate"

# JSON data to send in the request
data = {
    "model": "tinyllama",
    "prompt": "Why is the sky blue?",
    "stream": False,
}

# Headers specifying content type
headers = {
    "Content-Type": "application/json"
}

# Sending POST request to the API
response = requests.post(url, json=data, headers=headers)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    print("Response from ollama: \n")
    value = response.json()
    print("The value type of response: ", type(value))
    # print(response.json())
    print(value["response"])

else:
    print(f"Error: {response.status_code} - {response.text}")

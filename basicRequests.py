import requests

url = "https://www.example.com"

# Basic Get Request

response = requests.get(url)
print(response.text) # Return the result

# Basic Get Request With Headers

headers = {
  "content-type": "application/text"
}

response = requests.get(url, headers=headers)
print(response.text)

# Basic Post Request

response = requests.post(url)
print(response.text)

# Basic Post Request Json

payload = {
  "search": "Hello World"
}

response = requests.post(url, json=payload) # THIS WON'T AFFECT THE RESULT ON THIS SITE!!

# Basic Data Request Post Json

payload = {
  "search": "Hello World"
}

response = requests.post(url, data=payload) # THIS WON'T AFFECT THE RESULT ON THIS SITE!!

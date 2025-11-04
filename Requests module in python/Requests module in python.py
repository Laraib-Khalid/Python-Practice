# ✅ Install Required Libraries
# pip install beautifulsoup4
# pip install requests     # Recommended for making HTTP requests

import requests
from bs4 import BeautifulSoup

# ------------------ PART 1: Fetch & Parse Website Content ------------------

# Send GET request to Google
response = requests.get("https://www.google.com")

# Print the raw HTML response using Walrus operator (assign & print)
print(data := response.text)

# Print a line separator for clarity
print("-" * 300)

# Create a BeautifulSoup object to parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Format and display HTML structure nicely
print(soup.prettify())


# ------------------ PART 2: Send POST Request (JSON Data) ------------------

# API endpoint where we will send our POST request
url = "https://jsonplaceholder.typicode.com/posts"

# Data to send in JSON format
data = {
    "title": "harry",
    "body": "bhai",
    "userId": 12
}

# Setting headers to tell API we are sending JSON data
headers = {
    "Content-type": "application/json; charset=UTF-8"
}

# Sending POST request with JSON body & headers
response = requests.post(url, headers=headers, json=data)

# Print API response (server returns same data we sent)
print(response.text)



# ✅ 1️⃣ Simple GET Request

# Send a simple GET request to a website
response = requests.get("https://httpbin.org/get")

# Print response text (HTML or JSON content)
print(response.text)


# ✅ 2️⃣ GET Request + Check Status Code

url = "https://httpbin.org/get"
response = requests.get(url)

# Check if request was successful (status code 200)
if response.status_code == 200:
    print("✅ Request Successful")
    print(response.text)
else:
    print(f"❌ Request Failed with status {response.status_code}")



# ✅ 3️⃣ GET Request + Parse JSON Response

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# Convert JSON text into Python list/dict
users = response.json()

# Print all users' names
for user in users:
    print("Name:", user["name"])


# ✅ 4️⃣ Adding Headers (e.g., Browser User-Agent)

url = "https://httpbin.org/headers"

# Fake browser header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
print(response.json())


# ✅ 5️⃣ POST Request (Sending Form Data)

url = "https://httpbin.org/post"

# Form fields like HTML form data
data = {
    "username": "Laraib",
    "password": "1234"
}

response = requests.post(url, data=data)
print(response.json())  # server returns what we sent



# ✅ 6️⃣ POST Request (Sending JSON Data)

url = "https://httpbin.org/post"

# Data sent in JSON format
payload = {
    "id": 1,
    "task": "Learning Python Requests"
}

response = requests.post(url, json=payload)
print(response.json())



# ✅ 7️⃣ File Download Using requests

url = "https://www.example.com/sample.pdf"
file_name = "data.pdf"

# stream=True avoids loading whole file in memory
response = requests.get(url, stream=True)

with open(file_name, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        file.write(chunk)

print("✅ File Downloaded:", file_name)



# ✅ 8️⃣ Handling Request Timeout

try:
    response = requests.get("https://httpbin.org/delay/5", timeout=2)
    print(response.text)

except requests.exceptions.Timeout:
    print("⏳ Request timed out!")


# ✅ 9️⃣ Error Handling Example

url = "https://wrong-url-example.com"

try:
    response = requests.post(url)
    response.raise_for_status()  # raise error if status not 200
    print(response.text)

except requests.exceptions.RequestException as e:
    print("❌ Error:", e)



# ✅ 🔟 Download Image and Save

url = "https://picsum.photos/200"
image = requests.get(url)

with open("photo.jpg", "wb") as f:
    f.write(image.content)

print("✅ Image saved!")
# Example: Run 5 tasks in a thread pool
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Task {n} started")
    time.sleep(1)
    print(f"Task {n} finished")

# Run tasks concurrently
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(task, range(1, 6))

print("✅ All tasks complete!")


# ✅ Web Scraping with Threads (BeautifulSoup + Requests)
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

urls = [
    "https://example.com",
    "https://www.wikipedia.org",
    "https://www.python.org",
]

def fetch_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.text if soup.title else "No title found"
        print(f"{url} --> {title}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# Thread pool scraping
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(fetch_title, urls)

print("✅ Scraping completed!")



# ✅ Real Download Manager Example
import requests
from concurrent.futures import ThreadPoolExecutor

files = {
    "image1": "https://picsum.photos/200/300",
    "image2": "https://picsum.photos/200/301",
    "image3": "https://picsum.photos/200/302",
}

def download(name_url):
    name, url = name_url
    data = requests.get(url).content
    with open(f"{name}.jpg", "wb") as f:
        f.write(data)
    print(f"✅ {name}.jpg downloaded")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(download, files.items())

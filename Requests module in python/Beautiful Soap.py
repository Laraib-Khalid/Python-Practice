# pip install tabulate

# ✅ Example 1: Get Page Title
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://www.wikipedia.org"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

title_tag = soup.title

if title_tag:
    print("Page Title:", title_tag.text)
else:
    print("❌ Title not found, response might be blocked or changed.")



# ✅ Example 2: Extract All Links From a Webpage

url = "https://www.python.org"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))



# ✅ Example 3: Extract All Paragraph Text

url = "https://www.bbc.com/news"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for p in soup.find_all('p'):
    print(p.text)
    print("-" * 50)


# ✅ Example 4: Find Specific Elements (e.g., headlines)

url = "https://www.bbc.com/news"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")

print("Headlines:\n")
for h in headlines:
    print("-", h.text.strip())



# ✅ Example 5: Scrape Table from Website

url = "https://www.worldometers.info/world-population/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

data = []
for row in rows:
    cells = [cell.text.strip() for cell in row.find_all(["th", "td"])]
    data.append(cells)

# ✅ Print Header Dynamically
header = data[0]
print(" | ".join(f"{col:<25}" for col in header))
print("-" * (len(header) * 27))

# ✅ Print all rows
for row in data[1:]:
    print(" | ".join(f"{col:<25}" for col in row))



# ✅ Pretty Printed Table Using tabulate

url = "https://www.worldometers.info/world-population/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

data = []
for row in rows:
    cells = [cell.text.strip() for cell in row.find_all(["th", "td"])]
    data.append(cells)

# Print table nicely
print(tabulate(data, headers="firstrow", tablefmt="grid"))

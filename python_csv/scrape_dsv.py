# scrape_dsv.py
# Purpose: Scrape a table from the Wikipedia page about Delimiter-separated values

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# 1. Download the Wikipedia page
url = "https://en.wikipedia.org/wiki/Delimiter-separated_values"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
resp = requests.get(url, headers=headers)

resp.raise_for_status()   # stops the script if download fails

# 2. Parse the HTML
soup = BeautifulSoup(resp.text, "html.parser")
all_tables = soup.find_all("table")

# 3. Find the first table that looks valid (more than one column)
chosen = None
for table in all_tables:
    try:
        df = pd.read_html(str(table))[0]
        if df.shape[1] > 1:
            chosen = df
            break
    except Exception:
        continue

if chosen is None:
    raise SystemExit("No suitable table found on the page")

# 4. Save it to a CSV file inside python_csv
os.makedirs("python_csv", exist_ok=True)
chosen.to_csv("python_csv/dsv_example.csv", index=False)

# 5. Verify by reading it back and printing first rows
verify = pd.read_csv("python_csv/dsv_example.csv")
print(verify.head())

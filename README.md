# ST2195 — Practice Assignment 02

This repository contains my solutions for **Practice Assignment 02** of ST2195.  
The task was to scrape a table from the Wikipedia page  
**[Delimiter-separated values](https://en.wikipedia.org/wiki/Delimiter-separated_values)**  
using both **R** and **Python**, and save the results as CSV files.

---

## 📂 Repository Structure

```
st2195_assignment_2/
├─ README.md
├─ r_csv/
│  ├─ scrape_dsv.R
│  └─ dsv_example.csv
└─ python_csv/
   ├─ scrape_dsv.py
   └─ dsv_example.csv
```

---

## 🧮 Part 1: R Script

**File:** `r_csv/scrape_dsv.R`

**Description:**  
Uses the `rvest` library to:
1. Read the Wikipedia page HTML.
2. Extract the first table with more than one column.
3. Save it as `r_csv/dsv_example.csv`.

**Run command (from project root):**
```bash
Rscript r_csv/scrape_dsv.R
```

**Required package:**
```r
install.packages("rvest")
```

---

## 🐍 Part 2: Python Script

**File:** `python_csv/scrape_dsv.py`

**Description:**  
Uses `requests`, `BeautifulSoup`, and `pandas` to:
1. Download the same Wikipedia page.
2. Parse and extract the first valid HTML table.
3. Save it as `python_csv/dsv_example.csv`.

**Run command (from project root):**
```bash
python3 python_csv/scrape_dsv.py
```

**Required packages:**
```bash
pip install requests beautifulsoup4 pandas
```

---

## 📊 Output Example

Both scripts output a CSV file containing a table similar to:

| Delimiter-separated values | Delimiter-separated values.1 |
|-----------------------------|-------------------------------|
| Uniform Type Identifier (UTI) | public.delimited-values-text[1] |

---

## 🧠 Notes

- Both R and Python versions automatically create their respective folders (`r_csv/` and `python_csv/`) if they don’t exist.  
- The Python script includes a browser-like **User-Agent header** to avoid a `403 Forbidden` error from Wikipedia.  
- Both scripts print a preview of the scraped table to confirm successful scraping.

---

## ✨ Author
**Chek Wai June**  
ST2195 Practice Assignment 02  

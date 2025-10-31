{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # st2195_assignment_2\
\
This repository contains solutions for **Practice Assignment 02 (ST2195)**.\
\
### Contents\
- `r_csv/`: R script that scrapes an example CSV-like table from the Wikipedia page **\'93Delimiter-separated values\'94** and saves it as `dsv_example.csv`.\
- `python_csv/`: Python script that does the same scraping using Python.\
\
### How to use\
1. Run the R script in the `r_csv/` folder (requires the `rvest` library):\
   ```bash\
   Rscript r_csv/scrape_dsv.R\
   ```\
\
2. Run the Python script in the `python_csv/` folder (requires `requests`, `beautifulsoup4`, and `pandas`):\
   ```bash\
   python3 python_csv/scrape_dsv.py\
   ```\
\
Each script downloads a table from Wikipedia and saves it as `dsv_example.csv`.\
\
### Requirements\
- R (with the `rvest` package)\
- Python 3 (with `requests`, `beautifulsoup4`, and `pandas`)\
}
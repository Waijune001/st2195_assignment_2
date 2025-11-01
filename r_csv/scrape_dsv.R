# scrape_dsv.R
# Purpose: Scrape a table from the Wikipedia page about Delimiter-separated values

# Load the rvest package (install it first if you haven’t)
# install.packages("rvest")

library(rvest)

# URL of the page
url <- "https://en.wikipedia.org/wiki/Delimiter-separated_values"

# Read the HTML
page <- read_html(url)

# Extract all tables on the page
tables <- html_nodes(page, "table")

# Find the first table with more than one column
chosen <- NULL
for (i in seq_along(tables)) {
  tbl <- tryCatch(html_table(tables[[i]], fill = TRUE), error = function(e) NULL)
  if (!is.null(tbl) && ncol(tbl) > 1) {
    chosen <- tbl
    break
  }
}

# Stop if no table found
if (is.null(chosen)) {
  stop("No suitable table found on the page")
}

# Create folder if not existing
dir.create("r_csv", showWarnings = FALSE)

# Save the table as CSV
write.csv(chosen, file = "r_csv/dsv_example.csv", row.names = FALSE)

# Optional: read back to confirm
verify <- read.csv("r_csv/dsv_example.csv", stringsAsFactors = FALSE)
print(head(verify))


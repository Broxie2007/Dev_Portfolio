import requests
import csv
from bs4 import BeautifulSoup

# 1. Target URL
url = "http://books.toscrape.com/"

# 2. Get the HTML
# (Create a variable named 'response' and use requests.get)


# 3. Create the Soup
# (Create a variable named 'soup'. Pass response.text and "html.parser")


# 4. Find the Data
# (Find all the 'h3' tags and save them to a list called 'books')
# books = soup.find_all(...)

# 5. Save to CSV
print("Starting scrape...")

# Open a file named 'leads.csv'
with open("leads.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write the Header row first
    writer.writerow(["Book Title"])
    
    # Loop through the books list
    # for book in books:
        # Get the text from the book tag using book.text
        # title = ...
        
        # Write the row
        # writer.writerow([title])
        
        # Print it to terminal so we see it working
        # print(f"Saved: {title}")

print("Done! Check your leads.csv file.")

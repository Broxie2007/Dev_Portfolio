import requests
import csv
from bs4 import BeautifulSoup

# 1. Target URL
url = "http://books.toscrape.com/"

# 2. Get the HTML
response = requests.get(url)

# 3. Create the Soup
soup = BeautifulSoup(response.text, "html.parser")

# 4. Save to CSV
print("Starting scrape...")

with open("leads.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write the Header row (2 Columns now)
    writer.writerow(["Book Title", "Price"])
    
    # Find all the 'article' boxes (which contain both title and price)
    all_books = soup.find_all("article", class_="product_pod")
    
    for book in all_books:
        # Get the Title (inside h3 -> a)
        title = book.h3.a["title"]
        
        # Get the Price (inside p class='price_color')
        price = book.find("p", class_="price_color").text
        
        # Save both
        writer.writerow([title, price])
        print(f"Saved: {title} - {price}")

print("Done! Check leads.csv")
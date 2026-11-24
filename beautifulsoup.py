import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# Today's date for backup - because BBC homepage has no date
today = datetime.now().strftime("%d %b %Y")

data = []
seen = set()

for news in soup.find_all("h2"):
    headline = news.get_text(strip=True)
    # Skip small section titles like "Weekend Reads", "Premier League"
    if not headline or len(headline) < 20 or headline in seen:
        continue
    seen.add(headline)

    parent = news.find_parent("div")
    if parent:
        parent = parent.find_parent("div")
    if parent:
        parent = parent.find_parent("div")

    # Default date = Today
    date = today
    category = "News"

    if parent:
        # Try to get real date from <time> tag
        time_tag = parent.find("time")
        if time_tag:
            real_date = time_tag.get_text(strip=True)
            if real_date:
                date = real_date
            elif time_tag.get("datetime"):
                date = time_tag["datetime"][:10]

        # Category
        cat_tag = parent.find("span", attrs={"data-testid": "card-metadata-tag"})
        if cat_tag:
            category = cat_tag.get_text(strip=True)
        else:
            link_tag = news.find_parent("a")
            if link_tag and link_tag.get("href"):
                link = link_tag["href"]
                if "/news/" in link:
                    category = "News"
                elif "/sport/" in link:
                    category = "Sport"
                elif "/culture/" in link:
                    category = "Culture"
                elif "/business/" in link:
                    category = "Business"

    data.append([headline, date, category])

with open("news.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline", "Date", "Category"])
    writer.writerows(data)

print("News headlines saved successfully!")
print("Total headlines:", len(data))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup

# LIMIT NUMBER OF PAGES
MAX_PAGES = int(input("Enter max no of pages to scape:"))

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = "https://botpenguin.com/"
visited = set()
data = []

def scrape_page(url):
    try:
        # ✅ STOP condition
        if url in visited or len(visited) >= MAX_PAGES:
            return

        visited.add(url)

        print(f"Scraping ({len(visited)}/{MAX_PAGES}):", url)

        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract text
        for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
            text = tag.get_text(strip=True)
            if text and len(text) > 40:
                data.append(text)

        # Extract links
        links = driver.find_elements(By.TAG_NAME, "a")

        for link in links:
            href = link.get_attribute("href")

            if href and "botpenguin.com" in href:
                scrape_page(href)

    except Exception as e:
        print("Error:", e)

# Start scraping
scrape_page(base_url)

# Save data
df = pd.DataFrame(data, columns=["content"])
df.drop_duplicates(inplace=True)

df.to_csv("data.csv", index=False)

print("✅ Total pages visited:", len(visited))
print("✅ Total data collected:", len(df))

driver.quit()
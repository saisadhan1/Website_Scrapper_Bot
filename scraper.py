from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import time
import pandas as pd
from urllib.parse import urlparse, urljoin
from collections import deque

# ------------------------
# USER INPUT
# ------------------------
MAX_PAGES = int(input("Enter max number of pages to scrape: "))

# ------------------------
# CHROME SETUP
# ------------------------
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")        # Headless to prevent crashes
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ------------------------
# VARIABLES
# ------------------------
base_url = "https://botpenguin.com/"
visited = set()
data = []
queue = deque([base_url])  # Use queue instead of recursion for stability

# ------------------------
# SCRAPE LOOP
# ------------------------
while queue and len(visited) < MAX_PAGES:
    url = queue.popleft()
    
    if url in visited:
        continue

    try:
        print(f"Scraping ({len(visited)+1}/{MAX_PAGES}): {url}")
        driver.get(url)
        time.sleep(3)  # Wait for JS to load

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract text content
        for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
            text = tag.get_text(strip=True)
            if text and len(text) > 40:
                data.append(text)

        visited.add(url)

        # Extract links and add to queue
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            if href and "botpenguin.com" in urlparse(href).netloc:
                full_url = urljoin(base_url, href)
                if full_url not in visited:
                    queue.append(full_url)

    except WebDriverException as e:
        print("⚠ WebDriver error:", e)
        # Restart driver if crashed
        driver.quit()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        queue.append(url)  # Retry the current page

# ------------------------
# SAVE DATA
# ------------------------
df = pd.DataFrame(data, columns=["content"])
df.drop_duplicates(inplace=True)
df.to_csv("data.csv", index=False)

print("✅ Total pages visited:", len(visited))
print("✅ Total data collected:", len(df))

driver.quit()
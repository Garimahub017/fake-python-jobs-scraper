import requests
from bs4 import BeautifulSoup
import csv 

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)

jobs = soup.find_all("div", class_="card-content")

jobs_data = []

jobs_data = []

for job in jobs:
    title_element = job.find("h2", class_="title is-5")
    company_element = job.find("h3", class_="subtitle is-6 company")
    location_element = job.find("p", class_="location")
    link_element = job.find("a", class_="card-footer-item")

    title = title_element.get_text(strip=True) if title_element else "N/A"
    company = company_element.get_text(strip=True) if company_element else "N/A"
    location = location_element.get_text(strip=True) if location_element else "N/A"
    link = link_element.get("href") if link_element else "N/A"

    job_data = {
        "title": title,
        "company": company,
        "location": location,
        "url": link
    }

    jobs_data.append(job_data)


with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["title", "company", "location", "url"]
    )

    writer.writeheader()
    writer.writerows(jobs_data)
print("Scraping completed!")
print(f"Total jobs scraped: {len(jobs_data)}")

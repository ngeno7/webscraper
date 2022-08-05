import requests
import csv
from datetime import datetime

from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")
print(datetime.now())
rows = []
with open(datetime.now().strftime("%m%d%Y%H%M%S")+'_fake-jobs.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([
            'Title',
            'Company',
            'Location'
        ])
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")

        writer.writerow([
            title_element.text.strip(),
            company_element.text.strip(),
            location_element.text.strip()
        ])

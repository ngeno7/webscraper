from bs4 import BeautifulSoup
import requests

URL = "https://www.toyota.com/all-vehicles/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_='vehicles-grid')
print()
vehicles = results.find_all(class_='vehicle-card')

for vehicle in vehicles:
    print('Title:-------')
    print(vehicle.find(class_='title').text.strip())
    print('Price:-------')
    print(vehicle.find(class_='body-01').text.strip())
import pickle
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.one2car.com/en/cars-for-sale'
driver.get(url)
time.sleep(5) 
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
car_data = []
articles = soup.find_all('article')

for article in articles:
    title = article.find('h2').get_text(strip=True) if article.find('h2') else 'N/A'
    price_element = article.find('div', class_='listing__price')
    price = price_element.get_text(strip=True) if price_element else 'N/A'
    year = article.get('data-year', 'N/A')
    mileage_div = article.find('div', class_='item push-quarter--ends soft--right push-quarter--right')
    mileage = mileage_div.get_text(strip=True) if mileage_div else 'N/A'
    gearbox_div = article.find('div', class_='item push-quarter--ends')
    gearbox_type = gearbox_div.get_text(strip=True) if gearbox_div and 'icon--transmission' in str(gearbox_div) else 'N/A'
    location_div = article.find('div', class_='item push-quarter--ends', text=lambda t: t and 'Location' in t)    
    location = location_div.get_text(strip=True) if location_div else 'N/A'  
    link = article.find('a', href=True)['href'] if article.find('a', href=True) else 'N/A'

    car_data.append({
        'title': title,
        'price': price,
        'year': year,
        'mileage': mileage,
        'gearbox_type': gearbox_type,
        'location': location,
        'link': link
    })

with open('car_data.pkl', 'wb') as file:
    pickle.dump(car_data, file)

print("Data saved to car_data.pkl")

with open('car_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)

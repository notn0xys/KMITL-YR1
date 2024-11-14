from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pickle
car_data = []
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
for i in range(1,5):
    url = f"https://www.one2car.com/en/cars-for-sale?page_number={i}&page_size=26"
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        title = article.find('h2').get_text(strip=True) if article.find('h2') else 'N/A'
        price_element = article.find('div', class_='listing__price')
        price = price_element.get_text(strip=True) if price_element else 'N/A'
        year = article.get('data-year', 'N/A')
        mileage_div = article.find('div', class_='item push-quarter--ends soft--right push-quarter--right')
        mileage = mileage_div.get_text(strip=True) if mileage_div else 'N/A'
        listing_specs = article.find('div', class_='listing__specs')
        divs = listing_specs.find_all('div', class_='item')        
        gearbox_type = divs[1].get_text(strip=True) if divs[1] else 'N/A'
        location = divs[2].get_text(strip=True) if divs[2] else 'N/A'
        link = article.find('a', href=True)['href'] if article.find('a', href=True) else 'N/A'
        image_tag = article.find('img' , class_= "listing__img")
        image_url = image_tag['data-src'] if image_tag else 'N/A'
        car_data.append({
            'title': title,
            'price': price,
            'year': year,
            'mileage': mileage,
            'gearbox type': gearbox_type,
            'location': location,
            'link': link,
            'image': image_url
        })


with open('car_data.pkl', 'wb') as file:
    pickle.dump(car_data, file)

print("Data saved to car_data.pkl")
    
    
with open('car_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)


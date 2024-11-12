import pickle
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium to load JavaScript content
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.one2car.com/en/cars-for-sale'

# Open the page and wait for it to load fully
driver.get(url)
time.sleep(5)  # Adjust based on your connection speed and loading times

# Parse page content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Extract car details
car_data = []

# Target each <article> that represents a car listing
articles = soup.find_all('article')

for article in articles:
    try:
        # Extract title
        title_element = article.find('h2', class_='listing__title')
        title = title_element.get_text(strip=True) if title_element else 'N/A'
        
        # Extract price
        price_element = article.find('div', class_='listing__price')
        price = price_element.get_text(strip=True) if price_element else 'N/A'
        
        # Extract additional details from data attributes
        year = article.get('data-year', 'N/A')
        mileage = article.get('data-mileage', 'N/A') + ' km' if article.get('data-mileage') else 'N/A'
        gearbox_type = article.get('data-transmission', 'N/A')

        # Extract car link
        link_element = article.find('a', href=True)
        link = link_element['href'] if link_element else 'N/A'
        if not link.startswith('http'):
            link = 'https://www.one2car.com' + link  # Add domain if link is relative

        # Add the car's data to the list
        car_data.append({
            'title': title,
            'price': price,
            'year': year,
            'mileage': mileage,
            'gearbox_type': gearbox_type,
            'link': link
        })
    except AttributeError:
        continue  # Skip entries with missing data

# Save the data to a pickle file
with open('car_data.pkl', 'wb') as file:
    pickle.dump(car_data, file)

print("Data saved to car_data.pkl")

# Load and print the data to verify
with open('car_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)

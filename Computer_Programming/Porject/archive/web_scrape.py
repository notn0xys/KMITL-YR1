import requests
from bs4 import BeautifulSoup
import pickle
car_data = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
for i in range(1,6):
    url = f"https://www.one2car.com/en/cars-for-sale?page_number={i}&page_size=26"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
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
            location_div = article.find('div', class_='location-class-name')
            location = location_div.get_text(strip=True) if location_div else 'N/A'
            link = article.find('a', href=True)['href'] if article.find('a', href=True) else 'N/A'
            image_tag = article.find('img', class_='listing__img valign--top lazy-loaded')
            image = image_tag.get('data-src', 'N/A') if image_tag else 'N/A'
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
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code} from page{i}")


with open('car_data.pkl', 'wb') as file:
    pickle.dump(car_data, file)

print("Data saved to car_data.pkl")
    
    
with open('car_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)


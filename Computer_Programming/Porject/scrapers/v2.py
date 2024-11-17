from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_car_details(link):
    options = Options()


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get(link)
    time.sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    specifications_section = soup.find(id="tab-specifications")
    if not specifications_section:
        driver.quit()
        return {"error": "Specifications section not found"}

    specifications = {}
    spec_items = specifications_section.find_all("div", class_="o-grid o-grid--lg u-margin-ends-lg") 

    for item in spec_items:
        name_div = item.find("div", class_="u-width-1 u-padding-sides-md")
        if name_div and name_div.h3:
            spec_name = name_div.h3.text.strip()
        else:
            continue  

        value_div = item.find("div", class_="u-width-1/2 u-width-1@mobile u-padding-sides-md")
        if value_div:
            spec_value = value_div.text.strip()
        else:
            spec_value = "N/A"  

        specifications[spec_name] = spec_value

    driver.quit()

    return {
        "specifications": specifications,
    }

print(scrape_car_details('https://www.one2car.com/en/for-sale/mercedes-benz-glc350-e-4matic-amg-dynamic-bangkok-metropolitan-nonthaburi-rattanathibet/14346546'))

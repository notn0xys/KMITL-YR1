from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import PIL.Image
import customtkinter as ctk
import PIL 
import io
import webbrowser
import pickle
import requests
from PIL import Image
def update_info():
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
    print("Database Updated")
    with open('car_data.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
    print(loaded_data)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        self.bind("<F11>", lambda event: self.attributes("-fullscreen", not self.attributes("-fullscreen")))
        height = self.winfo_screenheight()
        self.geometry(f"{int(width * 0.8)}x{int(height * 0.8)}")
        self.minsize(800, 600)  
        self.maxsize(width, height)
        self.frames = {}
        self.title("Auto Shop")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        for F in (MainPage, SearchPage):
            frame = F(parent=self, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainPage")

    def show_frame(self, page_name):
        """Raise the selected page to the front"""
        frame = self.frames[page_name]
        frame.tkraise()

class Search:
    def on_search(self):
        pass

    def on_home(self):
        pass
    
    def load_car_data(self):
        try:
            with open('car_data.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("Pickle file not found.")
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []

    def make_page(self, x: dict = {}):
        for widget in self.winfo_children():
            widget.destroy()
        home_img = ctk.CTkImage(
            dark_image=Image.open("imgs\\home.png"), light_image=Image.open("imgs\\home.png"), size=(43, 43))
        my_img = ctk.CTkImage(
            dark_image=Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"), size=(43, 43))
        ctk.CTkButton(self, width=50, height=50, command=self.on_search, image=my_img, bg_color="transparent", text="").place(x=1350, y=3)
        ctk.CTkButton(self, width=50, height=50, command=self.on_home, image=home_img, bg_color="transparent", text="").place(x=1420, y=3)
    def backwards(self):
        self.page_multiplier -= 1
        self.create_page()

    def forward(self):
        self.page_multiplier += 1
        self.create_page()

class MainPage(ctk.CTkFrame, Search):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.last_page = False
        self.page_multiplier = 0
        self.controller = controller
        self.car_data = self.load_car_data()
        self.create_page()

    def show_car_details(self, car_id):
        car = self.car_data[car_id]
        print(f"Selected Car: {car['title']}, Price: {car['price']}, Details: {car}")

    def create_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"),size=(43,43))
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.e1 = ctk.CTkEntry(self, width=600, height=50)
        self.e1.grid(row=0, column=1, sticky= "nsew")
        search_button = ctk.CTkButton(self, width=50,height=50,command=self.on_search, image=my_img,bg_color="transparent",text="").place(x = 1075, y = 0)
        start_index = self.page_multiplier * 6
        end_index = start_index + 6
        for i, car in enumerate(self.car_data[start_index:end_index]):
            button_id = i + start_index
            car_button = ctk.CTkButton(
                self,
                width=450,
                height=300,
                text=f"{car['title']} - {car['price']}",
                command=lambda car_id=button_id: self.show_car_details(car_id)
            )
            car_button.grid(row=1 + i // 3, column=i % 3, pady=10, padx=(10,10),sticky="nsew",)
        if self.page_multiplier > 0:
            backbtn = ctk.CTkButton(self, text="Back", command=self.backwards)
            backbtn.grid(row=3, column=0, pady=(20, 0), padx=(10, 10), sticky="nsew")
        if end_index < len(self.car_data):
            next_button = ctk.CTkButton(self, text="Next", command=self.forward)
            next_button.grid(row=3, column=2, pady=(20, 0), padx=(10, 10), sticky="nsew")
        else:
            self.last_page = True

    def on_home(self):
        self.create_page()

    def on_search(self):
        self.controller.show_frame("SearchPage")


class SearchPage(ctk.CTkFrame, Search):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.page_multiplier = 0
        self.controller = controller
        self.car_data = self.load_car_data()
        self.create_page()

    def create_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"), size=(43, 43))
        home_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\home.png"), light_image=Image.open("imgs\\home.png"), size=(43, 43))
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.frame1 = ctk.CTkFrame(self, width=400, height=800)
        self.frame1.grid(row=0, column=0, sticky="nsew", rowspan=3)
        self.e1 = ctk.CTkEntry(self, width=600, height=50)
        self.e1.grid(row=0, column=1, sticky="n", padx=(15, 0))
        Home = ctk.CTkButton(self, width=50, height=50, command=self.on_home, image=home_img, bg_color="transparent", text="")
        Home.place(x=1025, y=0)
        
        for i in range(4):
            ctk.CTkButton(
                self, width=500, height=275, text=f"Car{(i + 1) + self.page_multiplier * 4}", command=self.make_page
            ).grid(row=1 + i // 2, column=i % 2 + 1, pady=(0, 10), padx=(0, 10), sticky="n")

    def on_search(self):
        self.create_page()

    def on_home(self):
        self.controller.show_frame("MainPage")

if __name__ == "__main__":
    app = App()
    app.mainloop() 
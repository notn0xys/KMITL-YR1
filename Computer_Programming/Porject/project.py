from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import PIL.Image
import customtkinter as ctk
import PIL 
from io import BytesIO
import pickle
import requests
import threading
import tkinter as tk
from tkinter import messagebox
from RangeSlider.RangeSlider import RangeSliderH 
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
def get_data(x:str) -> list:
    car_data = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = x
    driver.get(url)
    time.sleep(3)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        self.bind("<F11>", lambda event: self.attributes("-fullscreen", not self.attributes("-fullscreen")))
        height = self.winfo_screenheight()
        self.geometry(f"{int(width * 0.8)}x{int(height * 0.8)}")
        self.minsize(800, 650)  
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
    def scrape_car_details(self,link):
        options = Options()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(link)
        time.sleep(3)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        gallery_items = soup.find_all('div', class_='c-gallery__item')
        max_images = 3
        urls = []
        for item in gallery_items:
            img_tag = item.find('img') 
            if img_tag and 'src' in img_tag.attrs:
                urls.append(img_tag['src'])
            if len(urls) > max_images:
                break
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
            
            value_div = item.find_all("div", class_="u-width-1/2 u-width-1@mobile u-padding-sides-md")
            vallsit = []
            for values in value_div:
                if values:
                    vallsit.append(values.text.strip())
            specifications[spec_name] = vallsit

        driver.quit()

        return (specifications,urls)
        
    def on_search(self):
        pass

    def on_home(self):
        pass
    
    def load_car_data(self):
        try:
            with open('car_data.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("Pickle file not found, Please click on update database.")
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []

    def make_page(self, x: dict = {}):
        for widget in self.winfo_children():
            widget.destroy()

        def create_loading_popup():
            popup = ctk.CTkToplevel(self)
            popup.geometry("300x100")
            popup.title("Loading")
            popup.grab_set()  
            progress_label = ctk.CTkLabel(popup, text="Fetching car details...")
            progress_label.pack(pady=10)
            progress_bar = ctk.CTkProgressBar(popup, mode="indeterminate")
            progress_bar.pack(pady=10, padx=20, fill="x")
            progress_bar.start()  
            return popup

        loading_popup = create_loading_popup()
        def scrape_and_update():
            try:
                url = x['link']
                additional_data = self.scrape_car_details(url)  
            except Exception as e:
                self.after(0, lambda: messagebox.showerror("Error", f"Failed to fetch details: {e}"))
            finally:
                self.after(0, lambda: loading_popup.destroy())
                self.after(0, lambda: updatedetails(additional_data))
        def updatedetails(data):
            upper = ctk.CTkFrame(self)
            lower = ctk.CTkScrollableFrame(self)
            upper.grid(row = 0, sticky = 'nsew')
            lower.grid(row = 1, sticky = 'nsew')
            response = requests.get(data[1][0])
            pil_image = Image.open(BytesIO(response.content))
            pic1= ctk.CTkImage(pil_image,size=(800, 400))
            response = requests.get(data[1][1])
            pil_image = Image.open(BytesIO(response.content))
            pic2= ctk.CTkImage(pil_image,size=(400, 195))
            response = requests.get(data[1][2])
            pil_image = Image.open(BytesIO(response.content))
            pic3= ctk.CTkImage(pil_image,size=(400, 195))
            img_lab1 = ctk.CTkLabel(upper,image=pic1,text="",corner_radius = 5)
            img_lab2 = ctk.CTkLabel(upper,image=pic2,text="",corner_radius = 5)
            img_lab3 = ctk.CTkLabel(upper,image=pic3,text="",corner_radius = 5)
            img_lab1.grid(sticky = 'n', row = 0, rowspan = 2, column = 0 , padx = (20,5), pady = (10,0))
            img_lab2.grid(sticky = 'n', row = 0, column = 1, padx = (0,20), pady = (10,5))
            img_lab3.grid(sticky =  'n' , row = 1, column = 1, padx = (0,20), pady = (5,0))
        thread = threading.Thread(target=scrape_and_update)
        thread.start()
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
    def remove_percent(self,x):
        while True:
            if '%' in x:
                x = x[1:]
            else:
                return x
class MainPage(ctk.CTkFrame, Search):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.last_page = False
        self.page_multiplier = 0
        self.controller = controller
        self.car_data = self.load_car_data()
        self.create_page()
    def create_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"),size=(43,43))
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.e1 = ctk.CTkEntry(self, width=600, height=50)
        self.e1.grid(row=0, column=1, sticky= "nsew")
        search_button = ctk.CTkButton(self, width=50,height=50,command=self.on_search, image=my_img,bg_color="transparent",text="").place(x = 1100, y = 0)
        start_index = self.page_multiplier * 6
        end_index = start_index + 6
        for i, car in enumerate(self.car_data[start_index:end_index]):
            button_id = i + start_index
            response = requests.get(car['image'])
            pil_image = Image.open(BytesIO(response.content))
            pil_image = pil_image.resize((450, 250)) 
            ctk_image = ctk.CTkImage(pil_image,size=(450, 250))
            car_button = ctk.CTkButton(
                self,
                width=450,
                height=300,
                text=f"{car['title']} \n {car['price'] if '%' not in car['price'] else self.remove_percent(car['price'])}",
                image=ctk_image,
                compound="top",
                command=lambda car_id=button_id: self.make_page(self.car_data[car_id])
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
        self.minp = 0
        self.maxp = 4000000
        self.maxm = 200000
        self.minm = 0
        self.filter_text = ""
        self.selected_brand = "All Brands"
        self.brands = [
        "All Brands","Toyota", "Honda", "Nissan", "Ford", "Chevrolet", "BMW", 
        "Mercedes", "Audi", "Volkswagen", "Mazda", "Hyundai", 
        "Kia", "Suzuki", "Subaru", "Mitsubishi", 
        "Land Rover","Volvo", "Lexus", "Tesla", 
        "Porsche", "Ferrari", "Lamborghini", "McLaren", 
        "Bentley", "Dodge", "Jeep"
    ]
        self.create_page()
    def update_mile(self,*args):
        new_val = self.barmilage.getValues()
        self.minm = new_val[0]
        self.maxm = new_val[1]
    def update_price(self,*args):
        new_val = self.barprice.getValues()
        self.maxp = new_val[1]
        self.minp = new_val[0]
    def create_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"), size=(43, 43))
        home_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\home.png"), light_image=Image.open("imgs\\home.png"), size=(43, 43))
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.frame1 = ctk.CTkFrame(self, width=400, height=800)
        self.frame1.grid(row=0, column=0, sticky="nesw", rowspan=5, padx = (10,0))
        mile = ctk.CTkLabel(self.frame1,text="Mileage Range" , text_color= "white")
        mile.grid(row= 0, column = 0 , padx = 10, pady = (35,0))
        mileleft = ctk.DoubleVar(value=self.minm)
        mileright = ctk.DoubleVar(value=self.maxm)
        self.barmilage = RangeSliderH(self.frame1,[mileleft,mileright],padX=40,bgColor = '#333333',min_val= 0, max_val=200000,bar_color_inner = '#2fa572',font_size = 12,line_s_color = '#2fa572' , font_color= '#ffffff')
        self.barmilage.grid(row= 1,column=0,padx=10)
        mileleft.trace_add('write',self.update_mile)
        mileright.trace_add('write',self.update_mile)
        priceleft = ctk.DoubleVar(value= self.minp)
        priceright = ctk.DoubleVar(value= self.maxp)
        self.barprice = RangeSliderH(self.frame1, [priceleft,priceright],padX=40,bgColor='#333333',min_val=0,max_val=4000000,bar_color_inner = '#2fa572',font_size = 12,line_s_color = '#2fa572' , font_color= '#ffffff')
        priceleft.trace_add('write',self.update_price)
        priceright.trace_add("write",self.update_price)
        price = ctk.CTkLabel(self.frame1,text="Price Range", text_color="white")
        price.grid(row = 2,column = 0, padx = 10, pady = (  5,0))
        self.barprice.grid(row= 3,column=0,padx=10)

        self.e1 = ctk.CTkEntry(self, width=600, height=50,placeholder_text="Search")
        self.e1.grid(row=0, column=1, sticky="n", padx=(15, 0),pady =  (10,20))
        self.e1.insert(0,self.filter_text)
        self.e1.bind("<Return>", lambda event: self.apply())
        Home = ctk.CTkButton(self, width=50, height=50, command=self.on_home, image=home_img, bg_color="transparent", text="")
        Home.place(x=1050, y=10)
        brand_label = ctk.CTkLabel(self.frame1, text="Car Brand", text_color="white")
        brand_label.grid(row=4, column=0, padx=10, pady=(10, 0))

        self.brand_menu = ctk.CTkOptionMenu(self.frame1, values=self.brands, command=self.update_brand)
        self.brand_menu.set(self.selected_brand) 
        self.brand_menu.grid(row=5, column=0, padx=10, pady=(0, 20))
        filtered_data = []
        for car in self.car_data:
            try:
                mileage_str = car['mileage'].lower().replace('km', '').replace(',', '').strip()
                
                if '-' in mileage_str:
                    mileage_range = mileage_str.split('-')
                    max_mileage = int(mileage_range[1].replace('k', '').strip()) * 1000
                elif 'k' in mileage_str:
                    max_mileage = int(mileage_str.replace('k', '').strip()) * 1000
                else:
                    max_mileage = int(mileage_str.strip()) 

                price_str = car['price'].replace('Baht', '').replace(',', '').strip()
                if '%' in price_str:
                    price_str = self.remove_percent(price_str)
                elif 'Contact Seller' in price_str:
                    continue
                price = int(price_str)

            except Exception as e:
                print(f"Error parsing car data: {e}")
                continue
            
            if (self.minm <= max_mileage <= self.maxm 
                and self.minp <= price <= self.maxp 
                and (self.filter_text in car['title'].lower())
                and (self.selected_brand == "All Brands" or   self.selected_brand.lower() in car['title'].lower())
                ):
                filtered_data.append(car)

        start_index = self.page_multiplier * 4
        end_index = start_index + 4
        displayed_cars = filtered_data[start_index:end_index]
        for i, car in enumerate(displayed_cars):
            button_id = start_index + i
            response = requests.get(car['image'])
            pilimage = Image.open(BytesIO(response.content))
            pilimage = pilimage.resize((475,250))
            ctk_img = ctk.CTkImage(pilimage,size=(475,250))
            ctk.CTkButton(
                self, 
                width=500, 
                height=275, 
                text=f"{car['title']} \n {car['price'] if '%' not in car['price'] else self.remove_percent(car['price'])}",
                image = ctk_img,
                corner_radius= 10,
                compound= "top",
                command= lambda car_id = button_id: self.make_page(filtered_data[car_id])
            ).grid(row=1 + i // 2, column=i % 2 + 1, pady=(10, 10), padx=(10, 10), sticky="n")
        if self.page_multiplier > 0:
            backbtn = ctk.CTkButton(self, text="Back", command=self.backwards)
            backbtn.grid(row=3, column=1, pady=(20, 0), padx=(10, 10), sticky="nsew")
        if end_index < len(filtered_data):
            next_button = ctk.CTkButton(self, text="Next", command=self.forward)
            next_button.grid(row=3, column=2, pady=(20, 0), padx=(10, 10), sticky="nsew")
        else:
            self.last_page = True
        apply_btn = ctk.CTkButton(self.frame1,text="Apply",command=self.apply)
        apply_btn.grid(row = 6,column = 0 , sticky = 'nsew')
    def on_search(self):
        self.create_page()
    def apply(self):
        self.filter_text = self.e1.get().strip().lower()
        self.page_multiplier = 0
        self.create_page()
    def on_home(self):
        self.controller.show_frame("MainPage")
    def update_brand(self,selected_brand):
        self.selected_brand = selected_brand
if __name__ == "__main__":
    app = App()
    app.mainloop() 
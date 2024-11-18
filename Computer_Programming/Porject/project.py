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
import webbrowser
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def update_info():
    def create_loading_popup():
        popup = ctk.CTkToplevel()
        popup.geometry("300x100")
        popup.title("Loading")
        popup.grab_set()
        progress_label = ctk.CTkLabel(popup, text="Updating database...")
        progress_label.pack(pady=10)
        progress_bar = ctk.CTkProgressBar(popup, mode="indeterminate")
        progress_bar.pack(pady=10, padx=20, fill="x")
        progress_bar.start()
        return popup
    def update_db():
        try:
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
        except:
            print("Error Updating db")
        finally:
            if driver:
                driver.quit()
            popup.destroy()
    popup = create_loading_popup()
    thread = threading.Thread(target=update_db)
    thread.start()
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        self.bind("<F11>", lambda event: self.attributes("-fullscreen", not self.attributes("-fullscreen")))
        height = self.winfo_screenheight()
        self.geometry(f"{int(width * 0.82)}x{int(height * 0.82)}")
        self.minsize(800, 650)  
        self.maxsize(width, height)
        self.frames = {}
        self.data_manager = DataManager() 
        self.user_manager = UserManager()
        self.current_user = None 
        self.title("Auto Shop")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        for F in (LoginPage,RegisterPage,MainPage,SearchPage,AdminPage):
            frame = F(parent=self, controller=self, data_manager=self.data_manager)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("RegisterPage")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
class AdminPage(ctk.CTkFrame):
    def __init__(self,parent,controller,data_manager):
        super().__init__(parent)
        self.controller = controller
        self.data_manager = data_manager
        frame_for_btns = ctk.CTkFrame(self)
        frame_for_btns.grid(row = 1, column = 5, sticky = 'nsew')
        session_data = ctk.CTkLabel(self,text="Session Data")
        session_data.grid(row = 0, column = 0 , padx = 10 , pady = 5)
        all_time_data = ctk.CTkLabel(self , text="All time Data")
        all_time_data.grid(row = 0 , column = 1, padx = 10 , pady = 5)
        RefreshDb = ctk.CTkLabel(self, text="Refresh Database")
        RefreshDb.grid(row = 0, column = 5, padx = 10 , pady = 5) 
        refresh_button = ctk.CTkButton(frame_for_btns, text="Refresh Graphs", command=self.refresh_graphs)
        refresh_button.pack(pady = 10)
        self.graph_frame = ctk.CTkFrame(self)
        self.graph_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.total_graph_frame = ctk.CTkFrame(self)
        self.total_graph_frame.grid(row = 1, column = 1 ,pady=10, padx = 10, sticky = "nsew")
        self.plot_session_graph()
        self.plot_total_graph()
        refresh_db_btn = ctk.CTkButton(frame_for_btns,text='Refresh DB', command=self.refreshdb)
        refresh_db_btn.pack(pady = 10)
        return_btn = ctk.CTkButton(frame_for_btns,text="Return",command=self.swap_back)
        return_btn.pack(pady = 10)
        self.grid_rowconfigure(1, weight=2)  
        self.grid_rowconfigure(2, weight=3)  
        self.grid_columnconfigure(0, weight=2)  
        self.grid_columnconfigure(1, weight=2)  
        self.grid_columnconfigure(5, weight=1)
    def refreshdb(self):
        update_info()
        new_car_data = self.load_car_data()
        self.controller.frames["SearchPage"].car_data = new_car_data
        self.controller.frames["MainPage"].car_data = new_car_data
        self.controller.frames["MainPage"].create_page()
        self.controller.frames["SearchPage"].create_page()
    def refresh_graphs(self):
        self.plot_session_graph()
        self.plot_total_graph()
    def plot_session_graph(self):
        self.plot_graph(
            self.data_manager.get_clicked_cars(),
            "Session Clicks",
            self.graph_frame
        )
    def plot_total_graph(self):
        self.plot_graph(
            self.data_manager.get_all_time_clicks(),
            "All-Time Clicks",
            self.total_graph_frame
        )
    def plot_graph(self, data, title, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        car_names = list(data.keys())
        click_counts = list(data.values())

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(car_names, click_counts, color="skyblue") 
        ax.set_xlabel("Number of Clicks")
        ax.set_ylabel("Car Models")
        ax.set_title(title)
        ax.tick_params(axis='x', labelsize=8)  
        ax.tick_params(axis='y', labelsize=10)

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill="both", expand=True)
        canvas.draw()
        plt.close(fig)
    def swap_back(self):
        self.controller.show_frame("SearchPage")
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
class UserManager:
    def __init__(self, filename="users.pkl"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'wb') as file:
                pickle.dump({"users": []}, file)

    def load_users(self):
        with open(self.filename, 'rb') as file:
            return pickle.load(file)

    def save_users(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)

    def register_user(self, username, password, is_admin=False,favs = []):
        users = self.load_users()
        for user in users['users']:
                if user['username'] == username:
                    return False
        users["users"].append({"username": username, "password": password, "is_admin": is_admin,"favorites": favs})
        self.save_users(users)
        return True

    def authenticate_user(self, username, password):
        users = self.load_users()
        for user in users["users"]:
            if user["username"] == username and user["password"] == password:
                return user  
        return None
    def add_to_favorites(self, username, car):
        users = self.load_users()
        for user in users['users']:
            if user['username'] == username:
                if car not in user['favorites']:
                    user['favorites'].append(car)
                    self.save_users(users)
                    return True
        return False

    def remove_from_favorites(self, username, car):
        users = self.load_users()
        for user in users['users']:
            if user['username'] == username:
                if car in user['favorites']:
                    user['favorites'].remove(car)
                    self.save_users(users)
                    return True
        return False

    def get_favorites(self, username):
        users = self.load_users()
        for user in users['users']:
            if user['username'] == username:
                return user['favorites']
        return []
class LoginPage(ctk.CTkFrame):
    def __init__(self, parent,controller,data_manager):
        super().__init__(parent)
        self.controller = controller
        show = ctk.CTkLabel(self,text="Login" ,font=("Arial" , 18 ,"bold"))
        show.pack(pady = 20)
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username" , width= 250 , height= 40)
        self.username_entry.pack(pady=(10,10))
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*" , width= 250 , height= 40)
        self.password_entry.pack(pady=10)

        login_button = ctk.CTkButton(self, text="Login", command=self.login)
        login_button.pack(pady=10)

        register_button = ctk.CTkButton(self, text="Make an account", command=lambda: parent.show_frame("RegisterPage"))
        register_button.pack(pady=10)
        self.err_msg = ctk.CTkLabel(self,text='', font=("Arial" , 14 , "bold"),text_color= 'red')
        self.err_msg.pack(pady = 10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.username_entry.delete(0,ctk.END)
        self.password_entry.delete(0,ctk.END)
        if len(username) == 0 or len(password) == 0:
            self.err_msg.configure(text = "Invalid username or password")
            return
        user = self.controller.user_manager.authenticate_user(username, password)
        if user:
            self.controller.current_user = user
            self.err_msg.configure(text = '')
            self.controller.frames['SearchPage'].create_page()
            self.controller.show_frame("MainPage")
        else:
            self.err_msg.configure(text = "Wrong username or password")
class RegisterPage(ctk.CTkFrame):
    def __init__(self, parent,controller,data_manager):
        super().__init__(parent)
        self.controller = controller
        show = ctk.CTkLabel(self,text="Register" ,font=("Arial" , 18 ,"bold"))
        show.pack(pady = 20)
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width= 250 , height= 40)
        self.username_entry.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", width= 250 , height= 40)
        self.password_entry.pack(pady=10)
        self.admin_toggle = ctk.BooleanVar()
        admin_checkbox = ctk.CTkCheckBox(self, text="Register as Admin", variable=self.admin_toggle)
        admin_checkbox.pack(pady=10)

        register_button = ctk.CTkButton(self, text="Register", command=self.register)
        register_button.pack(pady=10)

        login_button = ctk.CTkButton(self, text="Sign in", command=lambda: parent.show_frame("LoginPage"))
        login_button.pack(pady=10)
        self.err_msg = ctk.CTkLabel(self,text='', font=("Arial" , 14 , "bold"),text_color= 'red')
        self.err_msg.pack(pady = 10)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.username_entry.delete(0,ctk.END)
        self.password_entry.delete(0,ctk.END)
        if len(username) == 0 or len(password) == 0:
            self.err_msg.configure(text = "Invalid username or password")
            return
        is_admin = self.admin_toggle.get()
        if self.controller.user_manager.register_user(username, password, is_admin):
            self.err_msg.configure(text = "")
            user = {'username': username,'password': password, 'is_admin':is_admin}
            self.controller.current_user = user
            self.controller.frames['SearchPage'].create_page()
            self.controller.show_frame("MainPage")
        else:
            self.err_msg.configure(text = "Username already exist")
class DataManager:
    def __init__(self,all_time_file="all_time_clicks.pkl"):
        self.clicked_cars = dict()
        self.all_time_file = all_time_file
        self.all_time_clicks = self.load_all_time_clicks()

    def add_car(self, car:dict):
        if car['title'][5:10] not in self.clicked_cars:
            self.clicked_cars[car['title'][5:17]] = 1
        else:
            self.clicked_cars[car['title'][5:17]] += 1
        self.update_all_time_clicks(car["title"][5:17])
    def get_cars(self):
        return self.clicked_cars
    def load_all_time_clicks(self):
        if os.path.exists(self.all_time_file):
            with open(self.all_time_file, "rb") as file:
                return pickle.load(file)
        return {}
    def update_all_time_clicks(self, car_title):
        self.all_time_clicks[car_title] = self.all_time_clicks.get(car_title, 0) + 1
        with open(self.all_time_file, "wb") as file:
            pickle.dump(self.all_time_clicks, file)
    def get_all_time_clicks(self):
        return self.all_time_clicks
    def get_clicked_cars(self):
        return self.clicked_cars
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
            vallist = []
            for values in value_div:
                if values:
                    vallist.append(values.text.strip())
            specifications[spec_name] = vallist

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
    def get_user_favorites(self):
        if self.controller.current_user:
            return self.controller.user_manager.get_favorites(self.controller.current_user["username"])
        return []
    def make_page(self, x: dict = {}):
        self.data_manager.add_car(x)
        self.amount = 12
        def hyperlink(link):
            webbrowser.open(link, autoraise = True)
        def select_period(choice):
            self.amount = int(choice)
        def open_toplevel():
            top = ctk.CTkToplevel(self)
            top.geometry("450x350")
            top.title("Interest Rate Calculator")
            top.grab_set()  
            title_label = ctk.CTkLabel(top, text="Interest Rate Calculator", font=("Arial", 16, "bold"))
            title_label.pack(pady=10)

            loan_amount_label = ctk.CTkLabel(top, text="Loan Amount:")
            loan_amount_label.pack(pady=(10, 0))
            filtered_price = self.remove_percent(x["price"])
            filtered_price = filtered_price.replace(",","")
            filtered_price = filtered_price.replace('Baht', "").strip()
            loan_amount_var = ctk.StringVar(value=filtered_price) 
            loan_amount_entry = ctk.CTkEntry(top, textvariable=loan_amount_var)
            loan_amount_entry.pack(pady=5)

            interest_rate_label = ctk.CTkLabel(top, text="Annual Interest Rate (%):")
            interest_rate_label.pack(pady=(10, 0))
            interest_rate_var = ctk.StringVar(value="5")
            interest_rate_entry = ctk.CTkEntry(top, textvariable=interest_rate_var)
            interest_rate_entry.pack(pady=5)

            loan_term_label = ctk.CTkLabel(top, text="Loan Term (Months):")
            loanterm = ctk.CTkOptionMenu(top,  values=["12","24","36","48","60","72","84"], command=select_period)
            loanterm.set("12")
            loan_term_label.pack(pady=(10, 0))
            loanterm.pack()

            result_label = ctk.CTkLabel(top, text="", font=("Arial", 12))
            result_label.pack(pady=(10, 0))
            def calc_amount():
                try:
                    loan_amount = float(loan_amount_var.get())
                    annual_rate = float(interest_rate_var.get())
                    loan_term = self.amount
                    monthly_rate = (annual_rate / 100) / 12
                    num_payments = loan_term 
                    if monthly_rate > 0:
                        monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
                    else:
                        monthly_payment = loan_amount / num_payments
                    result_label.configure(text=f"Monthly Payment: ฿{monthly_payment:.2f}")
                except ValueError:
                    result_label.configure(text="Invalid input. Please enter numeric values.")
            calc_btn = ctk.CTkButton(top,text="Calculate", command=calc_amount)
            calc_btn.pack()
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
            lower = ctk.CTkScrollableFrame(self,height=400)
            rightmost = ctk.CTkFrame(self,width = 500)
            upper.grid(row = 0,column = 0, columnspan = 4, sticky = 'nsew')
            lower.grid(row = 1,column = 0, columnspan = 4, sticky = 'nsew')
            rightmost.grid(row = 0, rowspan = 2,sticky = 'nsew',column = 4,columnspan = 2)
            home_img = ctk.CTkImage(dark_image=Image.open("imgs\\home.png"), light_image=Image.open("imgs\\home.png"), size=(43, 43))
            my_img = ctk.CTkImage(dark_image=Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"), size=(43, 43))
            ctk.CTkButton(rightmost, width=50, height=50, command=self.on_search, image=my_img, bg_color="transparent", text="").grid(sticky = 'n', row = 0,column = 0,pady = (20,0))
            ctk.CTkButton(rightmost, width=50, height=50, command=self.on_home, image=home_img, bg_color="transparent", text="").grid(sticky = 'n', row = 0,column = 1,pady = (20,0))
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
            column_count = 5
            for section, items in data[0].items():
                for index, item in enumerate(items):
                    items[index] = item.replace("\n", "\t")
            for i , (keys,values) in enumerate(data[0].items()):
                section_frame = ctk.CTkFrame(lower, corner_radius=5)
                section_frame.grid(row=i // column_count, column=i % column_count, padx=10, pady=10, sticky="nw")
                section_title = ctk.CTkLabel(section_frame, text=keys, font=("Arial", 14, "bold"))
                section_title.pack(pady=5, anchor="w")
                for item in values:
                    data_label = ctk.CTkLabel(section_frame, text=item, font=("Arial", 12),anchor="w")
                    data_label.pack(anchor="w", padx=5)
            title = ctk.CTkLabel(rightmost, text=f"{x['title']}",font=("Arial", 12))
            price = ctk.CTkLabel(rightmost, text=f"Price: {x['price']}",font=("Arial", 12))
            year = ctk.CTkLabel(rightmost, text=f"Year: {x['year']}",font=("Arial", 12))
            milage = ctk.CTkLabel(rightmost, text=f"Mileage: {x['mileage']}",font=("Arial", 12))
            location = ctk.CTkLabel(rightmost, text=f"Location: {x['location']}",font=("Arial", 12))
            buy_btn = ctk.CTkButton(rightmost,text='Buy Here',command=lambda: hyperlink(x['link']))
            intrest_clac = ctk.CTkButton(rightmost, text="Intrest rate calculator" , command=open_toplevel)
            is_favorite = x in self.get_user_favorites()
            def toggle_favorite():
                username = self.controller.current_user["username"]
                if x in self.get_user_favorites():
                    self.controller.user_manager.remove_from_favorites(username, x)
                    favorite_button.configure(text="🤍 Add to Favorites")
                else:
                    self.controller.user_manager.add_to_favorites(username, x)
                    favorite_button.configure(text="❤️ Remove from Favorites")
            favorite_button = ctk.CTkButton(rightmost,text="❤️ Remove from Favorites" if is_favorite else "🤍 Add to Favorites",command=toggle_favorite)        
            rows = 1
            for i in [title,price,year,milage,location,buy_btn,intrest_clac,favorite_button]:
                i.grid(sticky = 'n' , row = rows , column = 0 , columnspan = 2,pady = 5)
                rows += 1
    
        thread = threading.Thread(target=scrape_and_update)
        thread.start()

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
    def __init__(self, parent, controller,data_manager):
        super().__init__(parent)
        self.last_page = False
        self.page_multiplier = 0
        self.data_manager = data_manager
        self.controller = controller
        self.car_data = self.load_car_data()
        self.filter_text = ""
        self.create_page()
    def regen(self):
        if self.controller.current_user != None:
            self.controller.current_user = None
        self.car_data = self.load_car_data()
        self.on_home()
        self.controller.frames["SearchPage"].car_data = self.car_data 
        self.controller.frames["SearchPage"].create_page()


    def create_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        if len(self.car_data) == 0:
            self.temp = ctk.CTkToplevel(self)
            self.temp.geometry('450x300')
            get_data = ctk.CTkButton(self.temp,command=update_info,text="Get database")
            get_data.pack(pady = 10)
            def close_and_refresh():
                self.temp.destroy()
                self.regen()
                self.controller.show_frame("RegisterPage")
            refresh_frame = ctk.CTkButton(self.temp,command=close_and_refresh,text="Refresh app")
            refresh_frame.pack(pady = 10)
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"),size=(43,43))
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.e1 = ctk.CTkEntry(self, width=600, height=50)
        self.e1.grid(row=0, column=1, sticky= "nsew")
        self.e1.insert(0,self.filter_text)
        self.e1.bind("<Return>", lambda event: self.apply())
        search_button = ctk.CTkButton(self, width=50,height=50,command=self.on_search, image=my_img,bg_color="transparent",text="").place(x = 1100, y = 0)
        filtered_car = []
        
        for car in self.car_data:
            try:
                if self.filter_text.lower() in car['title'].lower():
                    filtered_car.append(car)
            except:
                print(car)
        start_index = self.page_multiplier * 6
        end_index = start_index + 6
        for i, car in enumerate(filtered_car[start_index:end_index]):
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
                command=lambda car_id=button_id: self.make_page(filtered_car[car_id])
            )
            car_button.grid(row=1 + i // 3, column=i % 3, pady=10, padx=(10,10),sticky="nsew",)
        if self.page_multiplier > 0:
            backbtn = ctk.CTkButton(self, text="Back", command=self.backwards)
            backbtn.grid(row=3, column=0, pady=(20, 0), padx=(10, 10), sticky="nsew")
        if end_index < len(filtered_car):
            next_button = ctk.CTkButton(self, text="Next", command=self.forward)
            next_button.grid(row=3, column=2, pady=(20, 0), padx=(10, 10), sticky="nsew")
        else:
            self.last_page = True

    def on_home(self):
        self.create_page()
    def apply(self):
        self.filter_text = self.e1.get().strip().lower()
        self.page_multiplier = 0
        self.create_page()
    def on_search(self):
        self.controller.show_frame("SearchPage")


class SearchPage(ctk.CTkFrame, Search):
    def __init__(self, parent, controller,data_manager):
        super().__init__(parent)
        self.page_multiplier = 0
        self.controller = controller
        self.car_data = self.load_car_data()
        self.minp = 0
        self.data_manager = data_manager
        self.maxp = 4000000
        self.maxm = 200000
        self.minm = 0
        self.view_favorites_only = tk.BooleanVar(value=False) 
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
    def toggle_view_favorites(self):
        self.page_multiplier = 0
        self.create_page()
    def get_user_favorites(self):
        if self.controller.current_user:
            return self.controller.user_manager.get_favorites(self.controller.current_user["username"])
        return []
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
        mile.pack(pady = (35,0))
        mileleft = ctk.DoubleVar(value=self.minm)
        mileright = ctk.DoubleVar(value=self.maxm)
        self.barmilage = RangeSliderH(self.frame1,[mileleft,mileright],padX=40,bgColor = '#333333',min_val= 0, max_val=200000,bar_color_inner = '#2fa572',font_size = 12,line_s_color = '#2fa572' , font_color= '#ffffff')
        self.barmilage.pack(pady = 10)
        mileleft.trace_add('write',self.update_mile)
        mileright.trace_add('write',self.update_mile)
        priceleft = ctk.DoubleVar(value= self.minp)
        priceright = ctk.DoubleVar(value= self.maxp)
        self.barprice = RangeSliderH(self.frame1, [priceleft,priceright],padX=40,bgColor='#333333',min_val=0,max_val=4000000,bar_color_inner = '#2fa572',font_size = 12,line_s_color = '#2fa572' , font_color= '#ffffff')
        priceleft.trace_add('write',self.update_price)
        priceright.trace_add("write",self.update_price)
        price = ctk.CTkLabel(self.frame1,text="Price Range", text_color="white")
        price.pack(pady = 10)
        self.barprice.pack(pady = 10)
        toggle_switch = ctk.CTkCheckBox(
            self.frame1,
            text="View Favorites Only",
            variable=self.view_favorites_only,
            onvalue=True,
            offvalue=False,
            command=self.toggle_view_favorites  
        )
        toggle_switch.pack(pady = 10)

        self.e1 = ctk.CTkEntry(self, width=600, height=50,placeholder_text="Search")
        self.e1.grid(row=0, column=1, sticky="n", padx=(15, 0),pady =  (10,20))
        self.e1.insert(0,self.filter_text)
        self.e1.bind("<Return>", lambda event: self.apply())
        Home = ctk.CTkButton(self, width=50, height=50, command=self.on_home, image=home_img, bg_color="transparent", text="")
        Home.place(x=1050, y=10)
        brand_label = ctk.CTkLabel(self.frame1, text="Car Brand", text_color="white")
        brand_label.pack(pady = 10)
        self.brand_menu = ctk.CTkOptionMenu(self.frame1, values=self.brands, command=self.update_brand)
        self.brand_menu.set(self.selected_brand) 
        self.brand_menu.pack(pady = 10)
        cars_to_display = self.get_user_favorites() if self.view_favorites_only.get() else self.car_data        
        filtered_data = []
        for car in cars_to_display:
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
            
            try:
                if (self.minm <= max_mileage <= self.maxm 
                    and self.minp <= price <= self.maxp 
                    and (self.filter_text.lower() in car['title'].lower())
                    and (self.selected_brand == "All Brands" or   self.selected_brand.lower() in car['title'].lower())
                    ):
                    filtered_data.append(car)
            except:
                print(car)
        if not filtered_data:
            no_data_label = ctk.CTkLabel(self, text="No cars match the criteria.")
            no_data_label.grid(row=1, column=0, columnspan=2, pady=20)
            return
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
        apply_btn.pack(pady = 10)
        log_out_btn = ctk.CTkButton(self.frame1,text='Log Out', command= self.log_out)
        log_out_btn.pack(pady = 10)
        if self.controller.current_user and self.controller.current_user["is_admin"]:
            manager_btn = ctk.CTkButton(self.frame1, text="Admin Panel", command=self.admin_swap)
            manager_btn.pack(pady = 10)
    def log_out(self):
        self.controller.current_user = None
        new_data_manager = DataManager()
        for frame_name, frame in self.controller.frames.items():
            if hasattr(frame, "data_manager"):
                frame.data_manager = new_data_manager
        self.controller.frames['SearchPage'].create_page()
        self.controller.frames['AdminPage'].refresh_graphs()
        self.controller.show_frame("RegisterPage")
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
    def admin_swap(self):
        self.controller.show_frame("AdminPage")
if __name__ == "__main__":   
    app = App()
    app.mainloop() 
import PIL.Image
import customtkinter as ctk
import PIL 
import io
import webbrowser
import pickle
import requests
from PIL import Image
from ip import search
class sp(search):
    def __init__(self,root):
        super().__init__()
        self.root = root
        self.create_page()
        print("In seach")
    def create_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"),size=(43,43),)
        home_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\home.png"), light_image=Image.open("imgs\\home.png"),size=(43,43),)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.root.title("AutoShop")
        self.root.after(0, lambda:self.root.state('zoomed'))
        self.e1 = ctk.CTkEntry(self.root,width=600, height=50)
        self.e1.place(x = 468,y=0)
        search_button = ctk.CTkButton(self.root, width=50,height=50,command=self.on_search, image=my_img,bg_color="transparent",text="").place(x = 1075, y = 0)
        Home = ctk.CTkButton(self.root, width=50,height=50,command=self.on_home, image=home_img,bg_color="transparent",text="").place(x = 1150, y = 0)
        for i in range(4):
            b = ctk.CTkButton(self.root, width=400 , height= 275 , text = f"Car{i + 1}", command= self.make_page,).grid(row = 1 + i//2, column = i // 2 + 1, pady = 15,padx = 20,sticky="w")
        
        
    def on_search(self):
        self.create_page()
    def on_home(self):
        from mp import main_page
        print("moving to main page")
        main_page(self.root)

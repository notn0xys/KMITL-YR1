import PIL.Image
import customtkinter as ctk
import PIL 
import io
import webbrowser
import pickle
import requests
from PIL import Image
from ip import search
class main_page(search):
    def __init__(self,root) -> None:
        self.search_mode = False
        super().__init__()
        self.root = root
        self.create_page()
        print("In main")
    def create_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.jpg"), light_image=Image.open("imgs\\wtf.jpg"),size=(43,43),)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.root.title("AutoShop")
        self.root.after(0, lambda:self.root.state('zoomed'))
        self.e1 = ctk.CTkEntry(self.root,width=600, height=50)
        self.e1.grid(row = 0, column = 1)
        search_button = ctk.CTkButton(self.root, width=50,height=50,command=self.on_search, image=my_img,bg_color="transparent").place(x = 1075, y = 0)
        for i in range(6):
            b = ctk.CTkButton(self.root, width=450 , height= 300 , text = f"Car{i + 1}", command= self.on_click,).grid(row = 1 + i//3, column = i % 3, pady = 10,padx = 10)
    def on_search(self):
        from sp import sp
        print("moving to search")
        sp(self.root)
    def on_home(self):
        self.create_page()
        
import PIL.Image
import customtkinter as ctk
import PIL 
import io
import webbrowser
import ZODB
import requests
from PIL import Image
#main page
class mp():
    def __init__(self) -> None:
        pass
class sp():
    def __init__(self) -> None:
        pass
class main():
    def __init__(self) -> None:
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("hi\wtf.jpg"), light_image=Image.open("hi\\wtf.jpg"),size=(43,43))
        self.search_mode = False
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.root = ctk.CTk()
        self.root.title("AutoShop")
        self.root.after(0, lambda:self.root.state('zoomed'))
        self.e1 = ctk.CTkEntry(self.root,width=600, height=50)
        self.e1.grid(row = 0, column = 1)
        search_button = ctk.CTkButton(self.root, width=50,height=50,command=self.on_click, image=my_img).place(x = 1075, y = 0)
        for i in range(6):
            b = ctk.CTkButton(self.root, width=450 , height= 300 , text = f"Car{i + 1}", command= self.on_click,).grid(row = 1 + i//3, column = i % 3, pady = 10,padx = 10)

        self.root.mainloop()
    def on_click(self):
        pass
    def search(self):
        self.search_mode = True
    def home(self):
        self.search_mode = False
    
main()
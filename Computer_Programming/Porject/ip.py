import customtkinter as ctk
import PIL
from PIL import Image
import PIL.Image
class search():
    def __init__(self) -> None:
        self.root = ctk.CTk()
    def on_search(self):
        pass
    def on_home(self):
        pass
    def make_page(self,x:dict = {}):
        for widget in self.root.winfo_children():
            widget.destroy()
        home_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\home.png"), light_image=Image.open("imgs\\home.png"),size=(43,43),)
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"),size=(43,43),)
        search_button = ctk.CTkButton(self.root, width=50,height=50,command=self.on_search, image=my_img,bg_color="transparent",text="").place(x = 1400, y = 3)
        home = ctk.CTkButton(self.root, width=50,height=50,command=self.on_home,image=home_img,bg_color="transparent",text="").place(x = 1470, y = 3)

    def create_page(self):
        pass
    def scroll(self,x:list,search_mode:bool):
        amount = 6
        if search_mode:
            amount = 4
        amount = len(x)//amount
        incriment = 0
    def on_click(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_page()





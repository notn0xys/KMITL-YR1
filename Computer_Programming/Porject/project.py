import PIL.Image
import customtkinter as ctk
import PIL 
import io
import webbrowser
import pickle
import requests
from PIL import Image
from archive.ip import search
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}+0+0")
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

    def make_page(self, x: dict = {}):
        for widget in self.winfo_children():
            widget.destroy()
        home_img = ctk.CTkImage(
            dark_image=Image.open("imgs\\home.png"), light_image=Image.open("imgs\\home.png"), size=(43, 43))
        my_img = ctk.CTkImage(
            dark_image=Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"), size=(43, 43))
        ctk.CTkButton(self, width=50, height=50, command=self.on_search, image=my_img, bg_color="transparent", text="").place(x=1350, y=3)
        ctk.CTkButton(self, width=50, height=50, command=self.on_home, image=home_img, bg_color="transparent", text="").place(x=1420, y=3)

class MainPage(ctk.CTkFrame, Search):
    page = 0
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_page()
    def create_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"),size=(43,43),)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.e1 = ctk.CTkEntry(self,width=600, height=50)
        self.e1.grid(row = 0, column = 1)
        search_button = ctk.CTkButton(self, width=50,height=50,command=self.on_search, image=my_img,bg_color="transparent",text="").place(x = 1075, y = 0)
        for i in range(6):
            b = ctk.CTkButton(self, width=450 , height= 300 , text = f"Car{i + 1}", command= self.make_page,).grid(row = 1 + i//3, column = i % 3, pady = 10,padx = 10)
        next_button = ctk.CTkButton(self, text="Next", command=lambda: self.controller.go_to_page("SearchPage"))
        next_button.grid(row=3, column=2, pady=(20, 0), padx=(10, 10), sticky="e")  # Adjust as necessary        
    def on_home(self):
        self.create_page()
    def on_search(self):
        self.controller.show_frame("SearchPage")
    def forward(self):
        page += 1
        self.create_page()    


class SearchPage(ctk.CTkFrame,Search):
    page = 0
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_page()
    def create_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        my_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\wtf.png"), light_image=Image.open("imgs\\wtf.png"), size=(43, 43))
        home_img = ctk.CTkImage(dark_image=PIL.Image.open("imgs\\home.png"), light_image=Image.open("imgs\\home.png"), size=(43, 43))
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.frame1 = ctk.CTkFrame(self, width=400, height=800)
        self.frame1.grid(row=0, column=0, sticky="nsew",rowspan = 3) 
        self.e1 = ctk.CTkEntry(self, width=600, height=50)
        self.e1.grid(row=0, column=1,sticky = "n",padx = (15,0))
        Home = ctk.CTkButton(self, width=50, height=50, command=self.on_home, image=home_img, bg_color="transparent", text="")
        Home.place(x=1025, y=0)
        for i in range(4):
            b = ctk.CTkButton(
                self, width=500, height=275, text=f"Car{i + 1}", command=self.make_page).grid(row=1 + i // 2, column=i % 2 + 1,  pady=(0, 10), padx=(0, 10), sticky="n")
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
    def on_search(self):
        self.create_page()
    def on_home(self):
        self.controller.show_frame("MainPage")
if __name__ == "__main__":
    app = App()
    app.mainloop()
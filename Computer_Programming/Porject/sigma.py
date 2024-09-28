import customtkinter as ctk
import PIL 
import io
import webbrowser
import ZODB
import requests

class main():
    def __init__(self) -> None:
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        root = ctk.CTk()
        root.title("AutoShop")
        root.geometry("1920x1080")
        root.mainloop()
main()
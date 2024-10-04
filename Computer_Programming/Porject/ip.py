import customtkinter as ctk

class search():
    def __init__(self) -> None:
        self.root = ctk.CTk()
    def on_search(self):
        pass
    def on_home(self):
        pass
    def make_page(self,x:dict):
        for widget in self.root.winfo_children():
            widget.destroy()
        name = x["name"]
        search_button = ctk.CTkButton(self.root, width=50,height=50,command=self.on_search, bg_color="transparent").place(x = 1075, y = 0)
        home = ctk.CTkButton(self.root, width=50,height=50,command=self.on_home, bg_color="transparent").place(x = 1200, y = 0)
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





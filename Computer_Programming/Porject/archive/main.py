import customtkinter as ctk
from archive.mp import main_page
def main():
    root = ctk.CTk()
    app = main_page(root)
    root.mainloop()
main()
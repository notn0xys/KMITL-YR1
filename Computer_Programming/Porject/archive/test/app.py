import customtkinter as ctk
from p1 import PageOne
from p2 import PageTwo

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.frames = {}  # Dictionary to hold references to each page
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Create both pages and store them
        for F in (PageOne, PageTwo):
            frame = F(parent=self, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
         # Show PageOne initially
        self.show_frame("PageOne")

    def show_frame(self, page_name):
        """Raise the selected page to the front"""
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()

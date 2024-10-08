import customtkinter as ctk

class PageOne(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.page_data = {"counter": 0}  # Example of data specific to PageOne
        
        label = ctk.CTkLabel(self, text="This is Page One")
        label.pack(pady=20)

        self.counter_label = ctk.CTkLabel(self, text=f"Counter: {self.page_data['counter']}")
        self.counter_label.pack()

        # Button to increment the counter (page-specific function)
        increment_button = ctk.CTkButton(self, text="Increment Counter", 
                                         command=self.increment_counter)
        increment_button.pack()

        # Button to switch to PageTwo
        switch_button = ctk.CTkButton(self, text="Go to Page Two", 
                                      command=lambda: controller.show_frame("PageTwo"))
        switch_button.pack()

    def increment_counter(self):
        """PageOne-specific method to update the counter"""
        self.page_data["counter"] += 1
        self.counter_label.configure(text=f"Counter: {self.page_data['counter']}")

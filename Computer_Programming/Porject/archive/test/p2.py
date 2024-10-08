import customtkinter as ctk

class PageTwo(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.page_data = {"message": "Hello from Page Two"}  # Example data specific to PageTwo
        
        label = ctk.CTkLabel(self, text="This is Page Two")
        label.pack(pady=20)

        self.message_label = ctk.CTkLabel(self, text=self.page_data["message"])
        self.message_label.pack()

        # Button to change the message (page-specific function)
        change_message_button = ctk.CTkButton(self, text="Change Message", 
                                              command=self.change_message)
        change_message_button.pack()

        # Button to switch to PageOne
        switch_button = ctk.CTkButton(self, text="Go to Page One", 
                                      command=lambda: controller.show_frame("PageOne"))
        switch_button.pack()

    def change_message(self):
        """PageTwo-specific method to update the message"""
        self.page_data["message"] = "Message updated!"
        self.message_label.configure(text=self.page_data["message"])

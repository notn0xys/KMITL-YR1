import customtkinter as ctk

class TwoPointSliderApp:
    def __init__(self, root):
        self.root = root

        # Create the first slider (lower bound) with customized appearance
        self.slider1 = ctk.CTkSlider(root, from_=0, to=100, command=self.update_range, width=300, button_color="blue")
        self.slider1.set(25)  # Set initial value for the lower slider
        self.slider1.place(x=50, y=100)

        # Create the second slider (upper bound) directly on top of the first slider
        self.slider2 = ctk.CTkSlider(root, from_=0, to=100, command=self.update_range, width=300, button_color="red")
        self.slider2.set(75)  # Set initial value for the upper slider
        self.slider2.place(x=50, y=100)

        # Labels to display the range
        self.label1 = ctk.CTkLabel(root, text=f"Lower Value: {self.slider1.get()}")
        self.label1.place(x=360, y=90)
        
        self.label2 = ctk.CTkLabel(root, text=f"Upper Value: {self.slider2.get()}")
        self.label2.place(x=360, y=130)

    def update_range(self, value):
        # Get the current values of the sliders
        lower_value = self.slider1.get()
        upper_value = self.slider2.get()

        # Ensure that the lower slider cannot go above the upper slider
        if lower_value > upper_value:
            self.slider1.set(upper_value)
        
        # Ensure that the upper slider cannot go below the lower slider
        if upper_value < lower_value:
            self.slider2.set(lower_value)

        # Update labels with the current values
        self.label1.configure(text=f"Lower Value: {self.slider1.get()}")
        self.label2.configure(text=f"Upper Value: {self.slider2.get()}")

root = ctk.CTk()
app = TwoPointSliderApp(root)
root.mainloop()

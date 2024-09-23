import tkinter as tk
class root():
    def __init__(self) -> None:
        root = tk.Tk()
        root.title("Drawww")
        self.canvas = tk.Canvas(root,bg="white",width=600,height=400)
        self.canvas.grid(row=0)
        self.canvas.bind("<B1-Motion>", self.click)
        l1 = tk.Label(root,text="Drag The mouse to draw").grid(row=1)
        btn1 = tk.Button(root,text="Clear",width=10,command=self.clear).grid(row=2)
        root.mainloop()
    def click(self,event):
        radius = 5
        oval = self.canvas.create_oval(event.x -5, event.y + 5, event.x + 5, event.y - 5 , fill="black" , tags="nigga")
    def clear(self):
        self.canvas.delete("nigga")
root()
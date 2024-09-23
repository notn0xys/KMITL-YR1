import tkinter as tk
class sol():
    def __init__(self) -> None:
        root = tk.Tk()
        self.canvas = tk.Canvas(root,bg="white",width=1000,height=500)
        self.canvas.pack()
        self.canvas.bind("<Button-1>" , self.checker)
        self.canvas.bind("<Button-3>" , self.remover)
        root.mainloop()
    def checker(self,event):
        self.canvas.create_oval(event.x-20,event.y+20,event.x+20,event.y-20,fill="white")
    def remover(self,event):
        overlap = self.canvas.find_overlapping(event.x,event.y,event.x,event.y)
        for i in overlap:
            self.canvas.delete(i)
sol()
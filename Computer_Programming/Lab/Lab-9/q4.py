import tkinter as tk
import tkinter.messagebox
import random
class run:
    def __init__(self) -> None:
        root = tk.Tk()
        self.canvas = tk.Canvas(root,bg="white",width=450,height=220)
        self.canvas.pack()
        self.canvas.create_rectangle(50,10,400,210) 
        self.canvas.bind("<Button-1>",self.checker)
        root.mainloop()
    def checker(self,event):
        if event.x > 400 or event.x < 50 or event.y > 210 or event.y < 10:
            tkinter.messagebox.showwarning(title="WARNING",message="Mouse pointer is not in the rectangle")
        else:
            list_of_col = ["Pink","Black","Green","Blue","Purple","White","Yellow","Orange"]
            meow = random.randint(0,7)
            self.canvas.create_oval(event.x-5,event.y+5,event.x+5,event.y-5,fill=list_of_col[meow])
run()
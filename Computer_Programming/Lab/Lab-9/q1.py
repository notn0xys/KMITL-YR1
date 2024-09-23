import tkinter as tk
class Button:
    def __init__(self):
        self.count = 0
        root = tk.Tk()
        self.l1 = tk.Label(root, text= self.count)
        btn1 = tk.Button(root,text="+",command=self.add)
        btn2 = tk.Button(root,text="-",command=self.minus)
        btn3 = tk.Button(root,text="Reset",command=self.reset)
        self.l1.grid(row=0,column=0, rowspan = 3)
        btn1.grid(row=0,column=1)
        btn2.grid(row=1,column=1)
        btn3.grid(row=2,column=1)
        root.mainloop()
    def add(self):
        self.count += 1
        self.l1["text"] = self.count
    def minus(self):
        self.count -= 1
        self.l1["text"] = self.count

    def reset(self):
        self.count = 0
        self.l1["text"] = self.count


Button()
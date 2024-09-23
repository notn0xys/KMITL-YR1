import tkinter as tk
from tkinter import messagebox
class solution():
    def __init__(self) -> None:
        root = tk.Tk()
        root.title("KMITL Phone")
        self.text = tk.StringVar()
        self.text.set("")
        l1 = tk.Label(textvariable=self.text,width=30).grid(row=0,column=0,columnspan=2)
        b1 = tk.Button(text=1,width=10,height=5,command = lambda: self.add("1")).grid(row=1,column=0)
        b2 = tk.Button(text=2,width=10,height=5,command = lambda: self.add("2")).grid(row=1,column=1)
        b3 = tk.Button(text=3,width=10,height=5,command = lambda: self.add("3")).grid(row=1,column=2)
        b4 = tk.Button(text=4,width=10,height=5,command = lambda: self.add("4")).grid(row=2,column=0)
        b5 = tk.Button(text=5,width=10,height=5,command = lambda: self.add("5")).grid(row=2,column=1)
        b6 = tk.Button(text=6,width=10,height=5,command = lambda: self.add("6")).grid(row=2,column=2)
        b7 = tk.Button(text=7,width=10,height=5,command = lambda: self.add("7")).grid(row=3,column=0)
        b8 = tk.Button(text=8,width=10,height=5,command = lambda: self.add("8")).grid(row=3,column=1)
        b9 = tk.Button(text=9,width=10,height=5,command = lambda: self.add("9")).grid(row=3,column=2)
        b10 = tk.Button(text="*",width=10,height=5,command = lambda: self.add("*")).grid(row=4,column=0)
        b11 = tk.Button(text=0,width=10,height=5,command = lambda: self.add("0")).grid(row=4,column=1)
        b12 = tk.Button(text="#",width=10,height=5,command = lambda: self.add("#")).grid(row=4,column=2)
        b13 = tk.Button(text="Talk",width=15,height=5,command = self.dail).grid(row=5,column=0,columnspan= 1)
        b14 = tk.Button(text="<",width=15,height=5,command = self.remove).grid(row=5,column=1,columnspan=1)
        root.mainloop()
    def remove(self):
        y = self.text.get()
        y = y[:-1]
        self.text.set(y)
    def dail(self):
        y = self.text.get()
        messagebox.showinfo("dialing",f"Dialing <{y}>")
    def add(self,x):
        y = self.text.get()
        z = y + x
        self.text.set(z)
solution()
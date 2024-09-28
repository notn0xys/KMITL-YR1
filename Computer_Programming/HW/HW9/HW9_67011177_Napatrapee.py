#Q1
import tkinter as tk
from tkinter import messagebox
class solution():
    def __init__(self) -> None:
        root = tk.Tk()
        root.title("KMITL Phone")
        self.text = tk.StringVar()
        self.text.set("")
        self.l1 = tk.Text(root,width=30,height=2)
        self.l1.grid(row=0,column=0,columnspan=3)
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
        y = self.l1.get("1.0", "end-1c")
        y = y[:-1]
        self.l1.delete('1.0', tk.END)
        self.l1.insert(tk.END, y)
    def dail(self):
        y = self.l1 .get("1.0", "end-1c")
        messagebox.showinfo("dialing",f"Dialing <{y}>")
    def add(self,x):
        y = self.l1.get("1.0", "end-1c")
        z = y + x
        self.l1.delete('1.0', tk.END)
        self.l1.insert(tk.END, z)
solution()
#Q2
import customtkinter as ctk
import PIL 
import io
import webbrowser
import ZODB
import requests
from PIL import Image
#main page
class mp():
    def __init__(self) -> None:
        pass
class sp():
    def __init__(self) -> None:
        pass
class main():
    def __init__(self) -> None:
        my_img = ctk.CTkImage(dark_image=PIL.open("img\wtf.png"), light_image=Image.open("img\wtf.png"),size=(50,50))
        self.search_mode = False
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.root = ctk.CTk()
        self.root.title("AutoShop")
        self.root.after(0, lambda:self.root.state('zoomed'))
        self.e1 = ctk.CTkEntry(self.root,width=600, height=50)
        self.e1.grid(row = 0, column = 1)
        search_button = ctk.CTkButton(self.root, width=50,height=50,command=self.on_click, image=my_img).place(x = 1075, y = 0)
        for i in range(6):
            b = ctk.CTkButton(self.root, width=450 , height= 300 , text = f"Car{i + 1}", command= self.on_click).grid(row = 1 + i//3, column = i % 3, pady = 10,padx = 10)

        self.root.mainloop()
    def on_click(self):
        pass
    def search(self):
        self.search_mode = True
    def home(self):
        self.search_mode = False
    
main()
#q3
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
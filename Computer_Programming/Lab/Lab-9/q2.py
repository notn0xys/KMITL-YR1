import tkinter as tk
import tkinter.messagebox
class main():
    def __init__(self) -> None:
        root = tk.Tk()
        self.text = tk.Text(root,height=1, width=10)
        self.text.pack()
        button1 = tk.Button(root,text="USD -> THB",command=self.usdthb).pack()
        button2 = tk.Button(root,text="THB -> USD",command=self.thbusd).pack()

        root.mainloop()
    def getinpuut(self):
        return self.text.get("1.0","end-1c")
    def usdthb(self):
        amount = float(self.getinpuut())
        tkinter.messagebox.showinfo(message=f"{amount:.2f} USD = {amount * 30:.2f} THB")
    def thbusd(self):
        amount = float(self.getinpuut())
        tkinter.messagebox.showinfo(message=f"{amount:.2f} THB = {amount / 30:.2f} USD")
main()
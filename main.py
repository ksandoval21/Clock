import tkinter
from tkinter import *
from tkinter.ttk import *
from time import strftime
top = tkinter.Tk()
p1 = PhotoImage(file="download.png")
top.iconphoto(False, p1)
top.title("GUI Clock")
top.resizable(0, 0)
def time():
    string = strftime("%I:%M:%S %p")
    clockTime.config(text=string)
    clockTime.after(1000, time)
clockTime = tkinter.Label(
    top, font=("calibri", 48, "bold"), background="black", foreground="white"
)
clockTime.pack(anchor="center")
time()
top.mainloop()
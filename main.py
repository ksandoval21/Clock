import tkinter as tk
from time import strftime

top= tk.Tk()
top.title('Clock')
top.resizable(0,0)
current_time=strftime("%I:%M:%S %p")
clock_label=tk.Label(top, font=('calibri', 40, 'bold'), bg="white", fg="pink", text=current_time)
clock_label.grid(row=0, column=0)
top.mainloop() 


def display_time():
    current_time=strftime("%M:%S:%p")
    clock_label.config(text=current_time)
    clock_label.after(200, display_time)

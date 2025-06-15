from tkinter import *
from tkinter.ttk import *
import time

window=Tk()
window.geometry("400x400")

box=Spinbox(window, from_=1, to=100)
box.pack(padx=10,pady=10)

box1=Spinbox(window, from_=0.1, to=20.1,increment=0.1 )
box1.pack(padx=10,pady=10)

list=["Apple", "Green", "Violin","Maths"]

box=Spinbox(window, value=list)
box.pack(padx=10,pady=10)

window.mainloop()
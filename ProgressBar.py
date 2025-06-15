from tkinter import *
from tkinter.ttk import *
import time

window=Tk()
window.geometry("400x400")
progress=Progressbar(window,orient=HORIZONTAL,length=100,mode="determinate")

def progresscommand():
    progress["value"]=25
    window.update_idletasks()
    time.sleep(1)
    progress["value"]=50
    window.update_idletasks()
    time.sleep(1)
    progress["value"]=75
    window.update_idletasks()
    time.sleep(1)
    progress["value"]=100
    window.update_idletasks()
    time.sleep(1)

button=Button(window,text="This is a button",command=progresscommand)
button.pack(padx=10,pady=10)

progress.pack(padx=10,pady=50)


progress1=Progressbar(window,orient="horizontal",length=100,mode="indeterminate")
progress1.pack(padx=10,pady=80)
def progresscommand1():
    progress1.start(100)

button1=Button(window,text="This is a button",command=progresscommand1)
button1.pack(padx=10,pady=70)




window.mainloop()
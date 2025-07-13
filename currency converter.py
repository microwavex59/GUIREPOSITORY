from tkinter import *
import tkinter.font as font
def convert():
    rupees=entry1.get()
    if (rupees.replace("."," ",1).isdigit()):
        errormsg.grid_forget()
        fahrenheit=(int(rupees)/71.428)
        label3.config(text=(f"Amt in USD is {fahrenheit : .2f}" ))
    else:
        errormsg.grid(row=3,column=0,columnspan=3)
        
    
window=Tk()
window.title("interface")
window.geometry("600x400")
window.configure(bg="blue")
window.resizable(width=False, height=False)
label1=Label(window, text="INR -> USD",font=font.Font(size=20,weight="bold"),bg="blue",fg="yellow")
label1.pack()
frame1=Frame(window,relief=RIDGE,bg="blue")
frame1.pack()
label2=Label(frame1,text="Input amt of Rs :",font=font.Font(size=15))
label2.grid(row=0,column=0)
entry1=Entry(frame1)
entry1.grid(row=0,column=2)
button1=Button(frame1,text="Convert",font=font.Font(size=15,weight="bold"),command=convert)
button1.grid(row=1,column=1)
label3=Label(frame1,width=60,height=1)
label3.grid(row=2,column=0,columnspan=3)
errormsg=Label(frame1, text="please enter valid input")

window.mainloop()

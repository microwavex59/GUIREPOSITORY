from tkinter import *
window=Tk()
window.title("interface")
window.geometry("400x400")
window.configure(bg="red")

label1=Label(window,text="label 1",width=6,height=5,bg="blue",fg="white",font="courier 10 italic",anchor="n")
label1.grid(row=0,column=0)
label2=Label(window,text="label 2",width=6,bg="green",fg="red",font="arial")
label2.grid(row=0,column=1)
label3=Label(window,text="label 3",width=6,bg="orange",fg="green",font="times")
label3.grid(row=0,column=2)
label4=Label(window,text="label 4",width=12,bg="purple",fg="orange")
label4.grid(row=1,column=0,columnspan=2,ipadx=3)
label5=Label(window,text="label 5",width=6,bg="blue",fg="yellow")
label5.grid(row=1,column=2)


window.mainloop()
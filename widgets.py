from tkinter import *
window=Tk()
window.title("interface")
window.geometry("400x400")
window.configure(bg="red")

#creating label and other widgets using the pack method
#label1=Label(window,text="Hello")
#label1.pack(pady=25)
#Entry1=Entry(window)
#Entry1.pack()
#button1=Button(window,text="Enter",command=window.destroy)
#button1.pack()

#creating label and other widgets using the grid method
label1=Label(window,text="Hello",font=("Arial",30),bg="blue",fg="white",bd=1,width=5,height=1,relief=SUNKEN,anchor=W)
label1.grid(row=0,column=0)
Entry1=Entry(window)
Entry1.grid(row=0, column=1)
button1=Button(window,text="Enter",command=window.destroy)
button1.grid(row=1,column=0,columnspan=2)



window.mainloop()
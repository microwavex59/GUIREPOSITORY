from tkinter import *
window=Tk()
window.title("interface")
window.geometry("800x400")
window.configure(bg="red")

label1=Label(window,text="Email",font=("Arial",15),bg="gray",fg="black",bd=1,width=5,height=1,anchor=W)
label1.place(x=50,y=50)
Entry1=Entry(window)
Entry1.place(x=200, y=50)

label2=Label(window,text="Password",font=("Arial",15),bg="gray",fg="black",bd=1,width=10,height=1,anchor=W)
label2.place(x=40,y=100)
Entry2=Entry(window)
Entry2.place(x=200, y=100)

label3=Label(window,text="What food would you like? Chicken sandwich, veg sandwich, blt, none",font=("Arial",15),bg="gray",fg="black",bd=1,width=60,height=1,anchor=W)
label3.place(x=40,y=150)
Entry3=Entry(window)
Entry3.place(x=150, y=175)

label4=Label(window,text="What drink would you like : Cola, fanta, orange Juice, water, none",font=("Arial",15),bg="gray",fg="black",bd=1,width=60,height=1,anchor=W)
label4.place(x=40,y=200)
Entry4=Entry(window)
Entry4.place(x=150, y=225)


label5=Label(window,text="What desert would you like: ice cream, ice lolly, chocolate cake, none",font=("Arial",15),bg="gray",fg="black",bd=1,width=60,height=1,anchor=W)
label5.place(x=40,y=250)
Entry5=Entry(window)
Entry5.place(x=150, y=275)

spin1=Spinbox(window, from_=0, to=10)
spin1.place(x=300,y=175)
spin2=Spinbox(window, from_=0, to=10)
spin2.place(x=300,y=225)
spin3=Spinbox(window, from_=0, to=10)
spin3.place(x=300,y=275)

button1=Button(window,text="Confirm Order",command=window.destroy)
button1.place(x=200,y=350)
window.mainloop()
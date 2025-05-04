from tkinter import *
window=Tk()
window.title("interface")
window.geometry("400x400")
window.configure(bg="red")
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)

frame1=Frame(window,borderwidth=3,relief="ridge",bg="blue")
frame1.grid(padx=50,pady=50,sticky="nsew")
frame1.columnconfigure(0,weight=1)
frame1.columnconfigure(1,weight=1)
frame1.rowconfigure(0,weight=1)

frame2=Frame(window,borderwidth=3,relief="ridge")
frame2.grid(row=0,column=0,padx=50,pady=50,sticky="nsew")

frame3=Frame(window,borderwidth=3,relief="ridge")
frame3.grid(row=0,column=1,padx=50,pady=50,sticky="nsew")

label1=Label(frame2,text="Hello")
label1.pack()

label2=Label(frame3,text="Michael")
label2.pack()
window.mainloop()
from tkinter import *
import calendar
def showcal():
    window2=Tk()
    window2.title("interface")
    window2.geometry("850x500")
    window2.configure(bg="blue")
    fetch_year=int(entry1.get())
    cal=calendar.calendar(fetch_year)
    calyear=Text(window2,font=("courier", 12))
    calyear.insert(END, cal)
    calyear.grid(row=5,column=2,padx=20,pady=40)
    window2.mainloop()
    
    

if __name__=="__main__":
    window1=Tk()
    window1.title("interface")
    window1.geometry("400x400")
    window1.configure(bg="red")
    label1=Label(window1, text="CALENDAR", width=60, height=5, bg="gray", fg="black", font="times", anchor="nw")
    label1.place(x=0,y=0)
    label2=Label(window1, text="Enter Year", width=15, height=2, bg="green", fg="black", font="times", anchor="nw")
    label2.place(x=0,y=100)
    entry1=Entry(window1)
    entry1.place(x=0,y=150)
    button1=Button(window1,text="Show Calendar",command=showcal)
    button1.place(x=0,y=180)
    button2=Button(window1, text="Close",command=window1.destroy)
    button2.place(x=0,y=220)



    window1.mainloop()
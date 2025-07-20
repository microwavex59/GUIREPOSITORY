from tkinter import *
import tkinter.font as font

pscoreval=0
cscoreval=0
options=[("rock",0),("paper",1),("scissors",2)]
def cwin():
    global cscoreval,pscoreval
    cscoreval=+1
    win_msg.config(text="Computer won!")
    cscore.config(text=(f"Computer score: {cscoreval}"))
    pscore.config(text=(f"Player score={pscoreval}"))


def pwin():
    global cscoreval,pscoreval
    pscoreval=+1
    win_msg.config(text="Player won!")
    cscore.config(text=(f"Computer score: {cscoreval}"))
    pscore.config(text=(f"Player score={pscoreval}"))

def tie():
    global cscoreval,pscoreval
    win_msg.config(text="Tie !")
    cscore.config(text=(f"Computer score: {cscoreval}"))
    pscore.config(text=(f"Player score={pscoreval}"))
def playerchoice():
    global cscoreval, pscoreval
    print()






window=Tk()
window.title("interface")
window.geometry("800x400")
window.configure(bg="white")
msg=Label(window,text="Rock Paper Scissors",font=font.Font(size=20),fg="gray")
msg.pack()
win_msg=Label(window,text="Let's Begin",font=font.Font(size=20),fg="gray")
win_msg.pack()
frame1=Frame(window,relief="ridge",bg="yellow")
frame1.pack()
label2=Label(frame1,text="Your options",fg="gray")
label2.grid(row=0,column=0)
button1=Button(frame1,text="Rock",bg="red")
button1.grid(row=1,column=1)
button2=Button(frame1,text="Paper",bg="green",)
button2.grid(row=1,column=2)
button3=Button(frame1,text="Scissors",bg="blue")
button3.grid(row=1,column=3)
frame2=Frame(window,relief="ridge",bg="gray")
frame2.pack()
label3=Label(frame2,text="Score:")
label3.grid(row=0,column=0)
pchoice=Label(frame2,text="You selected:")
pchoice.grid(row=1,column=1)
pscore=Label(frame2,text="Player score:")
pscore.grid(row=1,column=2)
cchoice=Label(frame2,text="Computer selected:")
cchoice.grid(row=2,column=1)
cscore=Label(frame2,text="Computer score:")
cscore.grid(row=2,column=2)
window.mainloop()
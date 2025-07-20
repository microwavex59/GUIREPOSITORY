
from tkinter import *
import tkinter.font as font
import random
pscoreval=0
cscoreval=0
options=[("rock",0),("paper",1),("scissors",2)]
def cwin():
    global cscoreval,pscoreval
    cscoreval=cscoreval+1
    win_msg.config(text="Computer won!")
    cscore.config(text=(f"Computer score: {cscoreval}"))
    pscore.config(text=(f"Player score={pscoreval}"))


def pwin():
    global cscoreval,pscoreval
    pscoreval=pscoreval+1
    win_msg.config(text="Player won!")
    cscore.config(text=(f"Computer score: {cscoreval}"))
    pscore.config(text=(f"Player score={pscoreval}"))

def tie():
    global cscoreval,pscoreval
    win_msg.config(text="Tie !")
    cscore.config(text=(f"Computer score: {cscoreval}"))
    pscore.config(text=(f"Player score={pscoreval}"))
    
def playerchoice(playerinput):
    global cscoreval, pscoreval
    print(playerinput[0])
    computerinput=computerchoice()
    print(computerinput)
    pchoice.config(text="Your selection: " + playerinput[0])
    cchoice.config(text="Computer choice:"+ computerinput[0])
    if (computerinput==playerinput):
        tie()

        #if player uses rock
    if (playerinput[1]==0):
        #computer selects paper
        if (computerinput[1]==1):
            cwin()
            #computer selects scissors
        elif (computerinput[1]==2):
            pwin()
        #if player uses paper
    if (playerinput[1]==1):
        #if computer uses scissors
        if (computerinput[1]==2):
            cwin()
            #if computer uses rock
        elif (computerinput[1]==0):
            pwin()
            #if player uses scissors
    if (playerinput[1]==2):
        #computer uses rock
        if (computerinput[1]==0):
            cwin()
            #computer uses paper
        elif (computerinput[1]==1):
            pwin()

        

def computerchoice():
    return random.choice(options)




window=Tk()
window.title("interface")
window.geometry("800x400")
window.configure(bg="white")
msg=Label(window,text="Rock Paper Scissors",font=font.Font(size=20),fg="gray")
msg.pack(padx)
win_msg=Label(window,text="Let's Begin",font=font.Font(size=20),fg="gray")
win_msg.pack(padx)
frame1=Frame(window,relief="ridge",bg="yellow")
frame1.pack(padx)
label2=Label(frame1,text="Your options",fg="gray")
label2.grid(row=0,column=0)
button1=Button(frame1,text="Rock",bg="red",command=lambda: playerchoice(options[0]))
button1.grid(row=1,column=1)
button2=Button(frame1,text="Paper",bg="green",command=lambda: playerchoice(options[1]))
button2.grid(row=1,column=2)
button3=Button(frame1,text="Scissors",bg="blue"command=lambda: playerchoice(options[2]))
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

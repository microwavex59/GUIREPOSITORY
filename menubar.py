from tkinter import *
from tkinter.ttk import *
window=Tk()
window.title("interface")
window.geometry("800x400")
window.configure(bg="red")

#creating menu bar
menubar=Menu(window)

#adding file menu and commands
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)

#adding menu items to the menu
file.add_command(label="New file", command=None)
file.add_command(label="Open file", command=None)
file.add_command(label="Save file", command=None)
file.add_separator()
file.add_command(label="Exit file", command=window.destroy)

#adding viewmenu

view=Menu(menubar,tearoff=0)
menubar.add_cascade(label="View", menu=view)

view2=Menu(view,tearoff=1)

view.add_cascade(label="Zoom",menu=view2)
view2.add_command(label="Zoom in", command=None)
view2.add_command(label="Zoom out", command=None)
view2.add_command(label="Reset out", command=None)
view.add_separator()
view.add_checkbutton(label="Status bar", command=None)
view.add_checkbutton(label="Fullscreen", command=None)
#display menu
window.config(menu=menubar)

mainloop()
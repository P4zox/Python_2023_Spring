from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
root=Tk()
root.geometry('1000x300')
root.title("HW1-1")

def start():
    stringvar1.set("processing") 
def stop():
    stringvar1.set("done")

startbutton=Button(root,command=start,text=("start"))
startbutton.pack()
stopbutton=Button(root,command=stop,text=("stop"))
stopbutton.pack()
stringvar1=StringVar()
stringvar1.set("initialization")


statusBar=Label(root,relief="sunken",bg="black",fg="white",anchor=W,textvariable=stringvar1)

statusBar.pack(fill="x",side="bottom")

root.mainloop()
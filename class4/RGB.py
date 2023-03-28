from tkinter import *
from PIL import Image, ImageTk
# import ScrollFrame 這個元件
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as ttk
# 從tkinter中引入filedialog
from tkinter import filedialog



root=Tk()
root.geometry('500x370')
root.title("Color selecter")




def getValue(a):
    r=int(rscale.get())
    g=int(gscale.get())
    b=int(bscale.get())
    hex="#{:02x}{:02x}{:02x}".format(r,g,b)
    redVar.set("R: "+str(rscale.get()))
    greenVar.set("G: "+str(gscale.get()))
    blueVar.set("B: "+str(bscale.get()))
    color_status["bg"]=hex
    color_status["text"]=hex

title=Label(root,text="choose color(RGB)")
title.grid(row=0,column=0,columnspan=2,sticky=W)

redVar=StringVar()
redVar.set("R: 0")
greenVar=StringVar()
greenVar.set("G: 0")
blueVar=StringVar()
blueVar.set("B: 0")

colorVar=StringVar()
colorVar.set("#000000")

rscale=Scale(root,from_=0,to=255,orient=HORIZONTAL,length=300,command=getValue)
gscale=Scale(root,from_=0,to=255,orient=HORIZONTAL,length=300,command=getValue)
bscale=Scale(root,from_=0,to=255,orient=HORIZONTAL,length=300,command=getValue)

rlabel=Label(root,textvariable=redVar)
glabel=Label(root,textvariable=greenVar)
blabel=Label(root,textvariable=blueVar)

rlabel.grid(row=1,column=0,sticky=W)
rscale.grid(row=2,column=0,columnspan=3,sticky=W)
glabel.grid(row=3,column=0,sticky=W)
gscale.grid(row=4,column=0,columnspan=3,sticky=W)
blabel.grid(row=5,column=0,sticky=W)
bscale.grid(row=6,column=0,columnspan=3,sticky=W)


color_status=Label(root,text="",bg="white")
color_status.grid(row=8,column=0,columnspan=3,sticky=W+E+N+S)
root.mainloop()
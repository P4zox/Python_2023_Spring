from tkinter import *
from PIL import Image, ImageTk
# import ScrollFrame 這個元件
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as ttk

root=Tk()
root.geometry('300x300')
root.title("class2")

# place1=Label(root,text="where you want to go: ")
# place1=Label(root,text="Why are you gae: ")
# place1.grid(column=0,row=0,columnspan=2,sticky=W)

# def fuse():
#     totalfuse=(flight1.get()+" "+flight2.get()+" "+flight3.get())
#     statusBar["text"]=totalfuse

# flight1=StringVar()
# flight2=StringVar()
# flight3=StringVar()
# place=StringVar()
# russia=Radiobutton(root,text="Russia", variable=place, value="Russia")
# china=Radiobutton(root,text="China", variable=place, value="China")
# rickroll=Radiobutton(root,text="Rickroll Island", variable=place, value="Rickroll Island")
# russia.grid(column=0,row=1,sticky=W)
# china.grid(column=1,row=1,sticky=W)
# rickroll.grid(column=2,row=1,sticky=W)
# statusBar=Label(root,relief="sunken",bg="black",fg="white",anchor=W,textvariable=place,width=45)
# statusBar.grid(column=0,row=4,columnspan=4,sticky=W)
# russia.select()

# f1=Checkbutton(root,text="直機",variable=flight1,onvalue="直機 ",offvalue="",command=fuse)
# f2=Checkbutton(root,text="轉機一次",variable=flight2,onvalue="轉機一次",offvalue="",command=fuse)
# f3=Checkbutton(root,text="轉機兩次",variable=flight3,onvalue="轉機兩次",offvalue="",command=fuse)
# f1.grid(column=0,row=1,sticky=W)
# f2.grid(column=1,row=1,sticky=W)
# f3.grid(column=2,row=1,sticky=W)
# statusBar=Label(root,relief="sunken",bg="black",fg="white",anchor=W,width=45)
# statusBar.grid(column=0,row=4,columnspan=4,sticky=W)

# create a scroll frame widget
sframe1=ScrolledFrame(root,width=300,height=300)
sframe1.pack()
# Bind the arrow keys and scroll wheel
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# Create a frame within the ScrolledFrame
inner_frame=sframe1.display_widget(Frame)
button1=Button(inner_frame,text="1",height=5)
button2=Button(inner_frame,text="2",height=5)
button3=Button(inner_frame,text="3",height=5)
button4=Button(inner_frame,text="4",height=5)
button5=Button(inner_frame,text="5",height=5)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

root.mainloop()
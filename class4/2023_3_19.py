from tkinter import *
from PIL import Image, ImageTk
# import ScrollFrame 這個元件
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as ttk
# 從tkinter中引入filedialog
from tkinter import filedialog



root=Tk()
root.geometry('500x370')
root.title("class4")

# def get_year():
#     yearVar.set(str(year_spin.get())+" years old")

# # 建立字串變數
# yearVar=StringVar()
# yearVar.set("0 years old")

# # 建立 Scale 元件
# # year_scale=Scale(root,from_=0,to=100,orient=HORIZONTAL,length=300,command=get_year)
# # year_scale.grid(row=0,column=0,columnspan=3)

# # 建立 Spinbox
# year_spin=Spinbox(root,from_=0,to=100,command=get_year)
# year_spin.grid(row=0,column=0,columnspan=3)

# # 建立 Label
# yLabel=Label(root, textvariable=yearVar,bg="black",fg="white")
# yLabel.grid(row=1,column=0,columnspan=3,sticky=W+E)

def spin_num():
    hVar.set(str(height_spin.get()))

# 建立字串變數
hVar=StringVar()
hVar.set(0)
# 建立SpinBox
height_spin=Spinbox(root,from_=0,to=250,command=spin_num)
height_spin.grid(row=0,column=0,columnspan=3)
# 建立Label
hLabel=Label(root,textvariable=hVar) 
# OGC
hLabel.grid(row=1,column=0,columnspan=3,sticky=W+E)

root.mainloop()
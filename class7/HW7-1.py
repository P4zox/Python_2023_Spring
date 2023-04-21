from twilio.rest import Client
# 大多數常用操作，只需要用到 Path 類別
from pathlib import Path
import pygsheets
from tkinter import *
from PIL import Image, ImageTk
# import ScrollFrame 這個元件
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as ttk
# 從tkinter中引入filedialog
from tkinter import filedialog

root=Tk()
root.geometry('500x370')
root.title("class7")

def submit():
    ws.update_value("A1","Name")
    ws.update_value("B1","E-mail")
    ws.update_value("C1","Password")
    ws.update_value("D1","Phone Number")
    ws.update_value("A2",name_entry.get())
    ws.update_value("B2",email_entry.get())
    ws.update_value("C2",password_entry.get())
    ws.update_value("D2",phoneNum_entry.get())
    print("sign up successfully")

gc=pygsheets.authorize(service_file="C:/Users/halst/Documents/Python_2023_Spring/class7/light-quest-383512-ecae9c4fe19c.json")
sht=gc.open_by_url("https://docs.google.com/spreadsheets/d/1KGAqHO-yo-18AlEgsuihI3O9K5TtSjXV3zgvdHv9ZsQ/edit#gid=0")
# 利用 Index 選取工作表
ws=sht[0]
name=Label(root,text="name: ")
name_entry=Entry(root)
email=Label(root,text="e-mail: ")
email_entry=Entry(root)
password=Label(root,text="password: ")
password_entry=Entry(root)
phoneNum=Label(root,text="phone number: ")
phoneNum_entry=Entry(root,)
okay_button=Button(root,text="sign up!",command=submit)

name.grid(row=1,column=1)
name_entry.grid(row=2,column=1)
email.grid(row=3,column=1)
email_entry.grid(row=4,column=1)
password.grid(row=5,column=1)
password_entry.grid(row=6,column=1)
phoneNum.grid(row=7,column=1)
phoneNum_entry.grid(row=8,column=1)
okay_button.grid(row=9,column=1)


root.mainloop()
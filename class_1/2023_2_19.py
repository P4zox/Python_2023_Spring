# 引入 Pillow module
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
root=Tk()
root.geometry('1000x300')
root.title("class1")
# 開啟圖片
img=Image.open("C:/Users/halst/Downloads/logo_tree.png")
# 轉換為 tk 圖片物件
tk_img=ImageTk.PhotoImage(img)
# 設定程式 icon
root.iconphoto(True,tk_img)

table=ttk.Treeview(root,columns=['Product Name','Unit Price', 'Quantity'])
# create column title
table.heading('#0',text='Product Name')
table.heading('#1',text='Unit Price')
table.heading('#2',text='Quantity')
table.heading('#3',text='Subtotal')
table.column('#0',width=250,anchor=CENTER)
table.column('#1',anchor=CENTER)
table.column('#2',anchor=CENTER)
table.column('#3',anchor=CENTER)
table.tag_configure('totalcolor',background='#E7E2E2')
table.insert("",index='end',text='Sofa',values=('20000','2','40000'))
table.pack()
# status Bar
# start button function
# def start():
#     stringvar1.set("processing")
# # stop button function 
# def stop():
#     stringvar1.set("done")

# # # 建立 Label
# # label1=Label(root,text="flat",relief="flat")
# # label2=Label(root,text="flat",relief="groove")
# # label3=Label(root,text="flat",relief="raised")
# # label4=Label(root,text="flat",relief="ridge")
# # label5=Label(root,text="flat",relief="solid")
# # label6=Label(root,text="flat",relief="sunken")
# # # 加入視窗
# # label1.pack()
# # label2.pack()
# # label3.pack()
# # label4.pack()
# # label5.pack()
# # label6.pack()

# # start button object
# startbutton=Button(root,command=start,text=("start"))
# startbutton.pack()
# # stop button object
# stopbutton=Button(root,command=stop,text=("stop"))
# stopbutton.pack()
# 建立StringVar
# stringvar1=StringVar()
# stringvar1.set("initialization")

# 建立 Label
# statusBar=Label(root,relief="sunken",bg="black",fg="white",anchor=W,textvariable=stringvar1)
# 加入視窗
# statusBar.pack(fill="x",side="bottom")

root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
# import ScrollFrame 這個元件
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as ttk
# 從tkinter中引入filedialog
from tkinter import filedialog



root=Tk()
root.geometry('300x300')
root.title("class3")
# # sframe1=ScrolledFrame(root,width=300,height=100,bg="white")
# # sframe1.pack()
# # # Bind the arrow keys and scroll wheel
# # sframe1.bind_arrow_keys(root)
# # sframe1.bind_scroll_wheel(root)
# # # Create a frame within the ScrolledFrame
# # inner_frame=sframe1.display_widget(Frame)

# # # Bind the arrow keys and scroll wheel
# # sframe1.bind_arrow_keys(root)
# # sframe1.bind_scroll_wheel(root)
# # # Create a frame within the ScrolledFrame
# # inner_frame=sframe1.display_widget(Frame)
# # button1=Button(inner_frame,text="1",height=5)
# # button2=Button(inner_frame,text="2",height=5)
# # button3=Button(inner_frame,text="3",height=5)
# # button4=Button(inner_frame,text="4",height=5)
# # button5=Button(inner_frame,text="5",height=5)
# # button1.pack()
# # button2.pack()
# # button3.pack()
# # button4.pack()
# # button5.pack()

# def choose():
#     mystringvar.set(str(box.current()+1)+". "+box.get())
# def choose_brand():
#     stringvar1.set(listbox.get(listbox.curselection()))

# mystringvar=StringVar()

# # 建立下拉式選單 Combobox
# mylabel=Label(root,textvariable=mystringvar)
# mylabel.grid(column=0,row=0,columnspan=3,sticky=W)
# box=ttk.Combobox(root,values=["BMW","Mercedes Benz", "Audi"])
# box.grid(column=0,row=1,columnspan=3,sticky=W)
# mybutton=Button(root,text="okay",command=choose)
# mybutton.grid(column=0,row=2)


# # 宣告用於ListBox的文字變數
# stringvar1=StringVar()
# listVar=StringVar()
# # 建立list BMW
# BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
# Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
# Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]
# # 將多個選項內容存入listVar
# listVar.set(BMW)
# # 建立清單列表 ListBox
# listbox=Listbox(root,selectmode="extended",listvariable=listVar)
# # 加入列表選單
# # listbox.insert(1,"A1")
# # listbox.insert(2,"A2")
# # listbox.insert(3,"A3")
# listbox.grid(column=0,row=3)
# listbutton=Button(root,text="choose",command=choose_brand)
# listlabel=Label(root,textvariable=stringvar1)
# listbutton.grid(column=0,row=4)
# listlabel.grid(column=0,row=5)

# 單選檔案，並以String回傳路徑
def choose():
    filepath=filedialog.askopenfilename(title="選取照片",initialdir="C:/Users/halst/Downloads",multiple=False)
    img=Image.open(filepath)
    img=img.resize((200,200))
    global tkimg
    tkimg=ImageTk.PhotoImage(img)

    sus=Label(root,image=tkimg)
    sus.grid(column=0,row=0)

chooseb=Button(root,command=choose,text="choose")
chooseb.grid(column=0,row=1)
    
root.mainloop()
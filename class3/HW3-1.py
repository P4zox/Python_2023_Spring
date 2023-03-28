from tkinter import *
from PIL import Image, ImageTk
# import ScrollFrame 這個元件
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as ttk



# 建立好視窗
root=Tk()
root.geometry('300x300')
root.title("HW3-1")



def choose():
    mystringvar.set(str(box.current()+1)+". "+box.get())
    if box.get()=="BMW":
        listVar.set(BMW)
    elif box.get()=="Mercedes Benz":
        listVar.set(Mercedes)
    elif box.get()=="Audi":
        listVar.set(Audi)
    
def choose_brand():
    stringvar1.set(listbox.get(listbox.curselection()))

mystringvar=StringVar()

# 建立 ComboBox
mylabel=Label(root,textvariable=mystringvar)
mylabel.grid(column=0,row=0,columnspan=3,sticky=W)
box=ttk.Combobox(root,values=["BMW","Mercedes Benz", "Audi"])
box.grid(column=0,row=1,columnspan=3,sticky=W)
mybutton=Button(root,text="okay",command=choose)
mybutton.grid(column=0,row=2)



stringvar1=StringVar()
listVar=StringVar()

BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]

# 建立 ListBox
listbox=Listbox(root,selectmode="extended",listvariable=listVar)
listbox.grid(column=0,row=3)
listbutton=Button(root,text="choose",command=choose_brand)
listlabel=Label(root,textvariable=stringvar1)
listbutton.grid(column=0,row=4)
listlabel.grid(column=0,row=5)

root.mainloop()
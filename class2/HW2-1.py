from tkinter import *
from PIL import Image, ImageTk
# import ScrollFrame 這個元件
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as ttk

root=Tk()
root.geometry('300x100')
root.title("點餐系統")
sframe1=ScrolledFrame(root,width=300,height=100)
sframe1.pack()
# Bind the arrow keys and scroll wheel
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# Create a frame within the ScrolledFrame
root1=sframe1.display_widget(Frame)

def fuse():
    totalfuse=(m_food1.get()+" "+m_food2.get()+" "+m_food3.get()+" "+drink1.get()+" "+drink2.get()+" "+drink3.get())
    statusBar['text']=totalfuse

text1=Label(root1,text="主餐: ")
text1.pack()
text2=Label(root1,text="飲品")

m_food1=StringVar()
m_food2=StringVar()
m_food3=StringVar()
drink1=StringVar()
drink2=StringVar()
drink3=StringVar()

m1=Checkbutton(root1,text="和牛",variable=m_food1,onvalue="和牛",offvalue="",foreground="pink",command=fuse)
m2=Checkbutton(root1,text="伊比利豬",variable=m_food2,onvalue="伊比利豬",offvalue="",foreground="pink",command=fuse)
m3=Checkbutton(root1,text="海鮮",variable=m_food3,onvalue="海鮮",offvalue="",foreground="pink",command=fuse)
d1=Checkbutton(root1,text="莊園咖啡",variable=drink1,onvalue="莊園咖啡",offvalue="",foreground="pink",command=fuse)
d2=Checkbutton(root1,text="日月潭蜜香紅茶",variable=drink2,onvalue="日月潭蜜香紅茶",offvalue="",foreground="pink",command=fuse)
d3=Checkbutton(root1,text="伯爵奶茶",variable=drink3,onvalue="伯爵奶茶",offvalue="",foreground="pink",command=fuse)
statusBar=Label(root1,relief="sunken",bg="black",fg="white",anchor=W,width=45)
m1.pack()
m2.pack()
m3.pack()
text2.pack()
d1.pack()
d2.pack()
d3.pack()
statusBar.pack()



root.mainloop()
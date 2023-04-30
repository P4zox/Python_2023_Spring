from tkinter import *
from tkinter import messagebox
import tkvideo
import tkinter.ttk as ttk
from email.mime.text import MIMEText
# 如果想在電子郵件加入圖片，則需在Python專案中引用MIMEImage類別，並且引用pathlib函式庫來讀取圖片
# 引入MIMEImage 物件
from email.mime.image import MIMEImage
from pathlib import Path
# 引入 MIMEMultipart 物件
from email.mime.multipart import MIMEMultipart
# 引入smtplib物件
# Python專案中的電子郵件內容完成後，接下來就是設定Gmail的SMTP伺服器來寄送
import smtplib
import pygsheets
import pandas as pd
root=Tk()
root.geometry('895x675')
root.title("HGS Store Info")
root["bg"]="#5C564A"
from PIL import Image, ImageTk
logoimg=Image.open("Project/Images/290320ed30724fb0aa91d3da057caed0 (1).png")
# 轉換為 tk 圖片物件
tk_img=ImageTk.PhotoImage(logoimg)
# 設定程式 icon
root.iconphoto(True,tk_img)
gc=pygsheets.authorize(service_file="C:/Users/halst/Documents/Python_2023_Spring/class7/light-quest-383512-ecae9c4fe19c.json")
sht=gc.open_by_url("https://docs.google.com/spreadsheets/d/1KGAqHO-yo-18AlEgsuihI3O9K5TtSjXV3zgvdHv9ZsQ/edit#gid=0")
# 利用 Index 選取工作表
ws=sht[0]
a=""

def systems():
    def signup(password,mail,name):
        password1=password.get()
        mail1=mail.get()
        name1=name.get()
        print("Name: "+str(name1)+"\nEmail:"+str(mail1)+"\nPassword:"+str(password1))
        df = pd.DataFrame(ws.get_all_records())
        df.loc[len(df.index)] = [str(name1), str(mail1), str(password1)]
        print(df)
        ws.set_dataframe(df, 'A1')
        system.destroy()
    def login(password,mail,name):
        global a
        password2=password.get()
        mail2=mail.get()
        name2=name.get()
        df = pd.DataFrame(ws.get_all_records())
        df_result = df[df["E-mail"]==mail2]
        if len(df_result) >= 1:
            if df_result["Password"][0] == password2:
                a=mail2
                system.destroy()
                # 帳號密碼皆正確
            else:
                a=""
                messagebox.showwarning("warning","invalid password, \n please enter the information again.")
        else:
            a=""
            messagebox.showwarning("warning","invalid password/e-mail, \n please enter the information again.")    
        print(a)


    system=Toplevel(root)
    system.geometry("300x500")
    system.title("login/signup system")
    Name_L=Label(system,text="Name:")
    Name_E=Entry(system)
    Email_L=Label(system,text="E-mail:")
    Email_E=Entry(system)
    Password_L=Label(system,text="Passowrd:")
    Password_E=Entry(system)
    login_B=Button(system,text="login",command=lambda:login(password=Password_E,mail=Email_E,name=Name_E))
    signup_B=Button(system,text="signup",command=lambda:signup(password=Password_E,mail=Email_E,name=Name_E))
    Name_L.grid(row=0,column=0)
    Name_E.grid(row=1,column=0,columnspan=2,sticky=W)
    Email_L.grid(row=2,column=0)
    Email_E.grid(row=3,column=0,columnspan=2,sticky=W)
    Password_L.grid(row=4,column=0)
    Password_E.grid(row=5,column=0,columnspan=2,sticky=W)
    login_B.grid(row=6,column=0)
    signup_B.grid(row=6,column=1)


    system.mainloop()
def add(numlabel,pricelabel):
    numlabel['text'] = int(numlabel['text'])+1
    price=int(pricelabel['text'].split('.')[1].strip())
    total=int(totalval.get().split(':')[1].replace('元',"").strip())
    totalval.set('共消費: '+str(total+price)+" 元")
def minus(numlabel,pricelabel):
    if int(numlabel['text'])>0:
        numlabel['text']=int(numlabel["text"])-1
        price=int(pricelabel['text'].split('.')[1].strip())
        total=int(totalval.get().split(':')[1].replace('元',"").strip())
        totalval.set('共消費: '+str(total-price)+" 元")
    else:
        messagebox.showwarning("showwarning","The number of products can\'t be below 0.")
def infomation():
    info_win=Toplevel(root)
    info_win.geometry("1000x300")
    info_win.title("infomations")
    table=ttk.Treeview(info_win,columns=['Product Name','Unit Price', 'Quantity'])

    table.heading('#0',text='Product Name')
    table.heading('#1',text='Unit Price')
    table.heading('#2',text='Quantity')
    table.heading('#3',text='Subtotal')
    table.column('#0',width=250,anchor=CENTER)
    table.column('#1',anchor=CENTER)
    table.column('#2',anchor=CENTER)
    table.column('#3',anchor=CENTER)
    table.tag_configure('totalcolor',background='#E7E2E2')
    subtotal1=int(Product_price_label1['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    subtotal2=int(Product_price_label2['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    subtotal3=int(Product_price_label3['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    subtotal4=int(Product_price_label4['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    table.insert("",index='end',text='<Call of Duty>Modern Warfare II 2022',values=(Product_price_label1['text'].split('.')[1].strip(),Product_num_label1["text"],subtotal1))
    table.insert("",index='end',text='<Rainbow 6> Siege',values=(Product_price_label2['text'].split('.')[1].strip(),Product_num_label2["text"],subtotal2))
    table.insert("",index='end',text='<Fortnite> Chapter 4 Season 1',values=(Product_price_label3['text'].split('.')[1].strip(),Product_num_label3["text"],subtotal3))
    table.insert("",index='end',text='<PUBG> Mobile',values=(Product_price_label4['text'].split('.')[1].strip(),Product_num_label4["text"],subtotal4))
    total_lol=subtotal1+subtotal2+subtotal3+subtotal4
    table.insert("",index="end",text="total",values=("","",total_lol),tag="totalcolor")
    table.pack()
    info_win.mainloop()
    return total_lol
def totallynotrickroll():
    subtotal1=int(Product_price_label1['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    subtotal2=int(Product_price_label2['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    subtotal3=int(Product_price_label3['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    subtotal4=int(Product_price_label4['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    if a!="":
        result=messagebox.askquestion('Purchase','Are you sure to purchase the items?')
        print('user click '+result)
        if result=="yes":
            tex=MIMEText("You just buy a total of {},\n {}".format(subtotal1+subtotal2+subtotal3+subtotal4))
            user=a
    # 創建並設定 MIMEMultipart 物件
            content=MIMEMultipart() #建立 MIMEMultipart 物件
            content["subject"]="Your e-mail receipt from HSG" #郵件標題
            content["from"]="halstonchen1119@gmail.com" #寄件者
            content["to"]=user #收件者
            content.attach(tex) #郵件內容#郵件圖片內容
    # 建立smtplib物件
            smtp=smtplib.SMTP(host="smtp.gmail.com",port="587")
    # 利用 with 來自動釋放資源
            with open("class5/password.txt","r") as f:
                mailToken=f.read()
            with smtp: #利用 with 來自動釋放資源
                try:
                    smtp.ehlo() #驗證SMTP伺服器
                    smtp.starttls() #建立加密傳輸
                    smtp.login("halstonchen1119@gmail.com",mailToken)
                    smtp.send_message(content) #寄送郵件
                    print("Email is Sended completely!")
                    smtp.quit()
                except Exception as e:
                    print("Error message: ",e)
    else:
        messagebox.showwarning("warning","you have not login, please login and try again")
def mw2_info():
    def mw2():
        mw=Toplevel(mw2_choose)
        mw.geometry("1000x750")
        mw2=Label(mw)
        mw2.pack()
        player1=tkvideo.tkvideo("Project/Images/official-launch-trailer-call-of-duty-modern-warfare-ii.mp4",mw2,loop=1,size=(1000,750))
        player1.play()
        mw.mainloop()
    mw2_choose=Toplevel(root)
    mw2_choose.geometry("500x500")
    mw2_choose["bg"]="#5C564A"
    mw2_trailer_B=Button(mw2_choose,text="Trailer",fg="#F0E5A9",bg="#5C564A",width=10,command=mw2)
    mw2_trailer_B.grid(row=0,column=0,columnspan=10,sticky=W+E)
    mw2_description_L=Label(mw2_choose,text="Description",font=1000200,fg="#F0E5A9",bg="#5C564A")
    mw2_description_L.grid(row=1,column=0,columnspan=10,sticky=W)
    mw2_choose.mainloop()
def r6():
    r=Toplevel(root)
    r.geometry("1000x750")
    r6=Label(r)
    r6.pack()
    player2=tkvideo.tkvideo("Project/Images/yt5s.io-Inside Rainbow Official Trailer – Tom Clancy's Rainbow Six Siege-(480p).mp4",r6,loop=1,size=(1000,750))
    player2.play()
    r.mainloop()
def ft():
    f=Toplevel(root)
    f.geometry("1000x750")
    ft=Label(f)
    ft.pack()
    player3=tkvideo.tkvideo("Project/Images/yt5s.io-Fortnite Chapter 4 Season 1 Launch Trailer-(480p).mp4",ft,loop=1,size=(1000,750))
    player3.play()
    f.mainloop()
def pubg():
    p=Toplevel(root)
    p.geometry("1000x750")
    pu=Label(p)
    pu.pack()
    player4=tkvideo.tkvideo("Project/Images/yt5s.io-PUBG - Stand United_ PGC 2019 Trailer-(480p).mp4",pu,loop=1,size=(1000,750))
    player4.play()
    p.mainloop()

# row=1
title_img=Image.open('Project/Images/290320ed30724fb0aa91d3da057caed0 (1).png')
title_img=title_img.resize((64,64))
title_img=ImageTk.PhotoImage(title_img)
title_label=Label(root,image=title_img,bg="#5C564A")
title_label.grid(row=0,column=0,sticky=W)
theme_Button=Button(root,text="類型: 射擊",font=("Inter",10),fg="#F0E5A9",width=10,height=2,bg="#5C564A")
theme_Button.grid(row=0,column=2,sticky=W)
search_Entry=Entry(root,text="search a game",width=50)
search_Entry.grid(row=0,column=3,columnspan=3,sticky=W+E)
cart_img=Image.open('Project/Images/istockphoto-1206806317-612x612.png')
cart_img=cart_img.resize((28,30))
cart_img=ImageTk.PhotoImage(cart_img)
cart_Button=Button(root,image=cart_img,bg="#5C564A",command=totallynotrickroll)
cart_Button.grid(row=0,column=6,sticky=E)
option_Button=Button(root,text="登入/註冊",font=("Inter",10),fg="Black",bg="#F0E5A9",width=8,height=2,command=systems)
option_Button.grid(row=0,column=7,sticky=W)
# row=2
line_img=Image.open('Project/Images/urmo.png')
line_img=line_img.resize((880,2))
line_img=ImageTk.PhotoImage(line_img)
line_Label=Label(root,image=line_img,bg="#5C564A")
line_Label.grid(row=1,column=0,columnspan=8,sticky=N,pady=1)
# row=3
mw2_img=Image.open('Project/Images/W5uSEsW7yefCNTHatS03v5q7.jpg')
mw2_img=mw2_img.resize((220,250))
mw2_img=ImageTk.PhotoImage(mw2_img)
mw2_Label=Label(root,image=mw2_img,bg="#5C564A")
mw2_Label.grid(row=2,column=0,columnspan=2,sticky=W+E)
r6_img=Image.open('Project/Images/Carousel_BoxArt_1200x1600_1200x1600-6888b9d57181d8fcfb3472a7f70ecc49.png')
r6_img=r6_img.resize((220,250))
r6_img=ImageTk.PhotoImage(r6_img)
r6_Label=Label(root,image=r6_img,bg="#5C564A")
r6_Label.grid(row=2,column=2,columnspan=2,sticky=W+E)
fortnite_img=Image.open('Project/Images/MV5BNzU2YTY2OTgtZGZjZi00MTAyLThlYjUtMWM5ZmYzOGEyOWJhXkEyXkFqcGdeQXVyNTgyNTA4MjM@._V1_FMjpg_UX1000_.jpg')
fortnite_img=fortnite_img.resize((220,250))
fortnite_img=ImageTk.PhotoImage(fortnite_img)
fortnite_Label=Label(root,image=fortnite_img,bg="#5C564A")
fortnite_Label.grid(row=2,column=4,columnspan=2,sticky=W+E)
pubg_img=Image.open('Project/Images/MV5BMTRkMjg2NDEtYzIxYi00MzZlLTllNmQtOTE4YWMzNjIwZDNkXkEyXkFqcGdeQXVyNTgyNTA4MjM@._V1_.jpg')
pubg_img=pubg_img.resize((220,250))
pubg_img=ImageTk.PhotoImage(pubg_img)
pubg_Label=Label(root,image=pubg_img,bg="#5C564A")
pubg_Label.grid(row=2,column=6,columnspan=2,sticky=W+E)
# row=4
Product_name_label1=Button(root,text="<Call of Duty> Modern Wafare II 2022",font=("Inter",10),fg="#F0E5A9",bg="#5C564A",command=mw2_info)
Product_name_label1.grid(row=3,column=0,columnspan=2,padx=5,sticky=W)
Product_name_label2=Button(root,text="<Rainbow 6> Siege",font=("Inter",10),fg="#F0E5A9",padx=5,bg="#5C564A",command=r6)
Product_name_label2.grid(row=3,column=2,columnspan=2,padx=5,sticky=W+E)
Product_name_label3=Button(root,text="<Fortnite> Chapter 4 Season 1",font=("Inter",10),fg="#F0E5A9",bg="#5C564A",command=ft)
Product_name_label3.grid(row=3,column=4,columnspan=2,padx=5,sticky=W+E)
Product_name_label4=Button(root,text="<PUBG> Mobile",font=("Inter",10),fg="#F0E5A9",bg="#5C564A",command=pubg)
Product_name_label4.grid(row=3,column=6,columnspan=2,padx=5,sticky=W+E)
# row=5
Product_price_label1=Label(root,text="NT.2100",font=("Inter",10),fg="#F0E5A9",bg="#5C564A")
Product_price_label2=Label(root,text="NT.540",font=("Inter",10),fg="#F0E5A9",bg="#5C564A")
Product_price_label3=Label(root,text="NT.0",font=("Inter",10),fg="#F0E5A9",bg="#5C564A")
Product_price_label4=Label(root,text="NT.0",font=("Inter",10),fg="#F0E5A9",bg="#5C564A")
Product_price_label1.grid(row=4,column=0,padx=5,sticky=W)
Product_price_label2.grid(row=4,column=2,padx=5,sticky=W)
Product_price_label3.grid(row=4,column=4,padx=5,sticky=W)
Product_price_label4.grid(row=4,column=6,padx=5,sticky=W)
Product_minus_button1=Button(root,text="-",font=("Inter",12),fg="Black",bg="#F0E5A9",command=lambda:minus(Product_num_label1,Product_price_label1))
Product_num_label1=Label(root,text="0",font=("Inter",10),fg="White",bg="#5C564A")
Product_add_button1=Button(root,text="+",font=("Inter",12),fg="Black",bg="#F0E5A9",command=lambda:add(Product_num_label1,Product_price_label1))
Product_minus_button2=Button(root,text="-",font=("Inter",12),fg="Black",bg="#F0E5A9",command=lambda:minus(Product_num_label2,Product_price_label2))
Product_num_label2=Label(root,text="0",font=("Inter",10),fg="White",bg="#5C564A")
Product_add_button2=Button(root,text="+",font=("Inter",12),fg="Black",bg="#F0E5A9",command=lambda:add(Product_num_label2,Product_price_label2))
Product_minus_button3=Button(root,text="-",font=("Inter",12),fg="Black",bg="#F0E5A9",command=lambda:minus(Product_num_label3,Product_price_label3))
Product_num_label3=Label(root,text="0",font=("Inter",10),fg="White",bg="#5C564A")
Product_add_button3=Button(root,text="+",font=("Inter",12),fg="Black",bg="#F0E5A9",command=lambda:add(Product_num_label3,Product_price_label3))
Product_minus_button4=Button(root,text="-",font=("Inter",12),fg="Black",bg="#F0E5A9",command=lambda:minus(Product_num_label4,Product_price_label4))
Product_num_label4=Label(root,text="0",font=("Inter",10),fg="White",bg="#5C564A")
Product_add_button4=Button(root,text="+",font=("Inter",12),fg="Black",bg="#F0E5A9",command=lambda:add(Product_num_label4,Product_price_label4))
Product_minus_button1.grid(row=4,column=1,sticky=W)
Product_num_label1.grid(row=4,column=1)
Product_add_button1.grid(row=4,column=1,sticky=E)
Product_minus_button2.grid(row=4,column=3,sticky=W)
Product_num_label2.grid(row=4,column=3)
Product_add_button2.grid(row=4,column=3,sticky=E)
Product_minus_button3.grid(row=4,column=5,sticky=W)
Product_num_label3.grid(row=4,column=5)
Product_add_button3.grid(row=4,column=5,sticky=E)
Product_minus_button4.grid(row=4,column=7,sticky=W)
Product_num_label4.grid(row=4,column=7)
Product_add_button4.grid(row=4,column=7,sticky=E)
# row=6
banner_img=Image.open('Project/Images/istockphoto-1272531936-170667a.jpg')
banner_img=banner_img.resize((885,240))
banner_img=ImageTk.PhotoImage(banner_img)
banner_label=Label(root,image=banner_img,bg="#5C564A")
banner_label.grid(row=5,column=0,columnspan=8,sticky=W)
# row=7
newProduct_name_label1=Label(root,text="最新產品(如上)",font=("Bold",24),fg="#F0E5A9",bg="#5C564A")
newProduct_name_label1.grid(row=7,column=0,columnspan=4,padx=5,sticky=W)
totalval=StringVar()
totalval.set('共消費: 0 元')
totallabel=Label(root,textvariable=totalval,font=('Inter',18),bg='#5C564A',fg="#F0E5A9")
totallabel.grid(row=7,column=2,columnspan=2,sticky=W)
info_img=Image.open('Project/Images/info but better.png')
info_img=info_img.resize((30,30))
info_img=ImageTk.PhotoImage(info_img)
info_Button=Button(root,image=info_img,bg="#5C564A",command=infomation)
info_Button.grid(row=7,column=6,sticky=E)
quit_button=Button(root,text="離開",font=("Bold",18),fg="Black",bg="#F0E5A9",command=root.destroy)
quit_button.grid(row=7,column=7,padx=5,sticky=W+E)


root.mainloop()
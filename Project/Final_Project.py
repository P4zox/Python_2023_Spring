from tkinter import *
from tkinter import messagebox
import tkvideo
from tkscrolledframe import ScrolledFrame
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
root.geometry('975x675')
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

def login_signup_systems():
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
    system.geometry("250x250")
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
def reciept():
    subtotal1=int(Product_price_label1['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    subtotal2=int(Product_price_label2['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    subtotal3=int(Product_price_label3['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    subtotal4=int(Product_price_label4['text'].split('.')[1].strip())*int(Product_num_label1["text"])
    if a!="":
        result=messagebox.askquestion('Purchase','Are you sure to purchase the items?')
        print('user click '+result)
        if result=="yes":
            tex=MIMEText("You just buy a total of {}".format(subtotal1+subtotal2+subtotal3+subtotal4))
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
add_on_counter1=0
def mw2_info():
    global add_on_counter1
    add_on_counter1=0
    description_text="Call of Duty: Modern Warfare 2 is a first person shooter, and its gameplay revolves around fast-paced gunfights against enemy combatants. The player controls a soldier who can perform several actions, including jump, sprint, crouch, lay prone, and aim down their gun's iron sights. When the player is shot by an enemy, blood will splatter their heads-up display (HUD), denoting that they have taken damage; if the player avoids gunfire by taking cover, their health will recover. The HUD also displays other information, such as a compass, a mini-map, and the player's current ammunition count. The game features traditional guns, including assault rifles, shotguns, handguns, and sniper rifles. The player will be given specific guns at the beginning of each level, but may switch them out with another gun they find. Some guns have attachments, such as suppressors, and heartbeat sensors. The player can use grenades and flashbangs when faced with a large group of enemies, as well as a knife for close quarters combat.In some levels, the player will be given special equipment, such as night vision goggles, or a laser designator. Players can compete against each other in multiplayer. Call of Duty: Modern Warfare 2 has three different game modes: Campaign, Spec Ops, and Multiplayer. Campaign is a single-player mode where the player completes eighteen levels connected by an overarching plot. Each level features a series of objectives to fulfill, and the player will often switch characters between levels. If the player dies during a level, they will respawn at the most recent checkpoint. Levels can be played on one of four difficulties, and each level can be replayed after it has been completed. Spec Ops mode features twenty-three additional levels that can be played individually or cooperatively with a partner. These levels provide specific challenges, such as defusing three bombs within a short period of time. If one player is shot down while playing cooperatively, they will begin crawling, and can shoot enemies with a handgun. If they are not revived by the other player, then they will die and fail the level. There are five tiers of Spec Ops levels, with each tier harder than the previous. Only the first tier is available from the beginning, as later tiers can be unlocked with enough stars. The player earns stars by completing the levels on one of three difficulties, with the number of stars earned corresponding to the difficulty chosen. Multiplayer mode allows players to compete against each other in team-based and deathmatch-based game types on various maps. Each game type has an objective that requires unique strategies to complete. If the player kills three or more players in a row without dying, they achieve a killstreak, which gives the player a tactical advantage during a match. These include a Predator missile, a sentry gun, and a tactical nuke. Alternatively, if the player dies several times without a kill, they will be rewarded with a deathstreak bonus, which evens the match for the player. A match ends when either a team or player has reached a predefined number of points, or the allotted time expires in which case the team or player with the most points wins. The player's performance in multiplayer is tracked with experience points, which can be earned by killing opposing players, completing objectives, or by completing a match. As the player gains experience, they advance in level, unlocking new weapons. The player will also unlock perks, which modify gameplay elements such as unlimited sprint and increased bullet damage."
    def mw2():
        mw=Toplevel(mw2_choose)
        mw.geometry("1000x750")
        mw2=Label(mw)
        mw2.pack()
        player1=tkvideo.tkvideo("Project/Images/official-launch-trailer-call-of-duty-modern-warfare-ii.mp4",mw2,loop=1,size=(1000,750))
        player1.play()
        mw.mainloop()
    def addOn1():
        global add_on_counter1
        if add_on_counter1>0:
            messagebox.showwarning("showwarning","You just purchase the add on system")
        else:
            mw_price.set("NT. "+str(mw_price_rate+600))
            add_on_counter1+=1
    mw2_choose=Toplevel(root)
    mw2_choose.geometry("500x750")
    sframe1=ScrolledFrame(mw2_choose,width=500,height=750,bg="white")
    sframe1.grid(row=2,column=0,columnspan=4,sticky=W)
    sframe1.bind_arrow_keys(mw2_choose)
    sframe1.bind_scroll_wheel(mw2_choose)
    inner_frame=sframe1.display_widget(Frame)
    mw2_trailer_B=Button(inner_frame,text="Trailer",width=10,command=mw2)
    mw2_trailer_B.grid(row=0,column=0,columnspan=10,sticky=W+E)
    mw2_description_L=Label(inner_frame,text="Description",font=1000200)
    mw2_description_L.grid(row=1,column=0,columnspan=10,sticky=W)
    sframe2=ScrolledFrame(inner_frame,width=400,height=400,bg="white")
    sframe2.grid(row=2,column=0,columnspan=4,sticky=W)
    sframe2.bind_arrow_keys(inner_frame)
    sframe2.bind_scroll_wheel(inner_frame)
    inner_frame2=sframe2.display_widget(Frame)
    mw2_description_info=Message(inner_frame2,text=description_text,width=400)
    mw2_description_info.grid(row=0,column=0,columnspan=4,sticky=W)

    manticore_img=Image.open('Project\Images\capsule_616x353.jpg')
    manticore_img=manticore_img.resize((308,271))
    global manticore
    manticore=ImageTk.PhotoImage(manticore_img)
    manticore_B=Button(inner_frame,image=manticore,command=addOn1)
    manticore_L=Label(inner_frame,text="<Call of Duty> Pro Pack 3/Manticore : NT.600")
    manticore_B.grid(row=8,column=0,columnspan=8,sticky=W)
    manticore_L.grid(row=9,column=0,columnspan=8,sticky=W)

    mw2_choose.mainloop()
add_on_counter2=0
def r6_info():
    global add_on_counter2
    description_text="and published by Ubisoft. It was released worldwide for PlayStation 4, Windows, and Xbox One on December 1, 2015; the game was also released for PlayStation 5 and Xbox Series X/S exactly five years later on December 1, 2020. The title received a port for Google Stadia on June 30, 2021, and one for Amazon Luna in January 2022.[1][2] The game puts heavy emphasis on environmental destruction and cooperation between players. Each player assumes control of an attacker or a defender in different gameplay modes such as rescuing a hostage, defusing a bomb, and taking control of an objective within a room. The title has no campaign but features a series of short, offline missions called, situations that can be played solo. These missions have a loose narrative, focusing on recruits going through training to prepare them for future encounters with the White Masks, a terrorist group that threatens the safety of the world. Siege is an entry in the Rainbow Six series and the successor to Tom Clancy's Rainbow 6: Patriots, a tactical shooter that had a larger focus on narrative. After Patriots was eventually cancelled due to its technical shortcomings, Ubisoft decided to reboot the franchise. The team evaluated the core of the Rainbow Six franchise and believed that letting players impersonate the top counter-terrorist operatives around the world suited the game most. To create authentic siege situations, the team consulted actual counter-terrorism units and looked at real-life examples of sieges such as the 1980 Iranian Embassy siege. Powered by AnvilNext 2.0, the game also utilizes Ubisoft's RealBlast technology to create destructible environments.The game received an overall positive reception from critics, with praise mostly directed to the game's tense multiplayer and focus on tactics. However, the game was criticized for its progression system and its lack of content. Initial sales were weak, but the game's player base increased significantly as Ubisoft adopted a games as a service model for the game and subsequently released several packages of free downloadable content. Several years after the game's release, some critics regarded Siege as one of the best multiplayer games in the modern market due to the improvements brought by the post-launch updates. The company partnered with ESL to make Siege an esports game. In December 2020, the game surpassed 70 million registered players across all platforms. Rainbow Six Extraction, a spin-off game featuring Siege characters, was released in January 2022."
    def r6():
        r=Toplevel(root)
        r.geometry("1000x750")
        r6=Label(r)
        r6.pack()
        player2=tkvideo.tkvideo("Project/Images/yt5s.io-Inside Rainbow Official Trailer – Tom Clancy's Rainbow Six Siege-(480p).mp4",r6,loop=1,size=(1000,750))
        player2.play()
        r.mainloop()
    def addOn2():
        global add_on_counter2
        if add_on_counter2>0:
            messagebox.showwarning("showwarning","You just purchase the add on system")
        else:
            r6_price.set("NT. "+str(r6_price_rate+1490))
            add_on_counter2+=1
    r6_choose=Toplevel(root)
    r6_choose.geometry("500x750")
    r6_trailer_B=Button(r6_choose,text="Trailer",width=10,command=r6)
    r6_trailer_B.grid(row=0,column=0,columnspan=10,sticky=W+E)
    r6_description_L=Label(r6_choose,text="Description",font=1000200)
    r6_description_L.grid(row=1,column=0,columnspan=10,sticky=W)
    sframe1=ScrolledFrame(r6_choose,width=400,height=400,bg="white")
    sframe1.grid(row=2,column=0,columnspan=4,sticky=W)
    sframe1.bind_arrow_keys(r6_choose)
    sframe1.bind_scroll_wheel(r6_choose)
    inner_frame=sframe1.display_widget(Frame)
    sframe2=ScrolledFrame(inner_frame,width=400,height=400,bg="white")
    sframe2.grid(row=2,column=0,columnspan=4,sticky=W)
    sframe2.bind_arrow_keys(inner_frame)
    sframe2.bind_scroll_wheel(inner_frame)
    inner_frame2=sframe2.display_widget(Frame)
    r6_description_info=Message(inner_frame2,text=description_text,width=400)
    r6_description_info.grid(row=0,column=0,columnspan=4,sticky=W)

    welcomePack_img=Image.open('Project\Images\welcomePack.jpg')
    welcomePack_img=welcomePack_img.resize((180,260))
    global welcomePack
    welcomePack=ImageTk.PhotoImage(welcomePack_img)
    welcomePack_B=Button(inner_frame,image=welcomePack,command=addOn2)
    welcomePack_L=Label(inner_frame,text="<Rainbow 6 Seige> Welcome Pack : NT.1490")
    welcomePack_B.grid(row=8,column=0,columnspan=8,sticky=W)
    welcomePack_L.grid(row=9,column=0,columnspan=8,sticky=W)
    r6_choose.mainloop()
add_on_counter3=0
def ft_info():
    global add_on_counter3
    description_text="Fortnite is an online video game developed by Epic Games and released in 2017. It is available in three distinct game mode versions that otherwise share the same general gameplay and game engine: Fortnite Battle Royale, a free-to-play battle royale game in which up to 100 players fight to be the last person standing; Fortnite: Save the World, a cooperative hybrid tower defense-shooter and survival game in which up to four players fight off zombie-like creatures and defend objects with traps and fortifications they can build; and Fortnite Creative, in which players are given complete freedom to create worlds and battle arenas. Save the World and Battle Royale were released in 2017 as early access titles, while Creative was released on December 6, 2018. While the Save the World and Creative versions have been successful for Epic Games, Fortnite Battle Royale in particular became an overwhelming success and a cultural phenomenon, drawing more than 125 million players in less than a year, earning hundreds of millions of dollars per month. Fortnite as a whole generated $9 billion in gross revenue up until December 2019. Save the World is available only for Windows, macOS,[c] PlayStation 4, and Xbox One, while Battle Royale and Creative were released for all those platforms, and also for Nintendo Switch, iOS,[c] and Android devices.[c] The game also launched with the release of the ninth-generation PlayStation 5 and Xbox Series X/S consoles."    
    def ft():
        f=Toplevel(root)
        f.geometry("1000x750")
        ft=Label(f)
        ft.pack()
        player3=tkvideo.tkvideo("Project/Images/yt5s.io-Fortnite Chapter 4 Season 1 Launch Trailer-(480p).mp4",ft,loop=1,size=(1000,750))
        player3.play()
        f.mainloop()
    def addOn3():
        global add_on_counter3
        if add_on_counter3>0:
            messagebox.showwarning("showwarning","You just purchase the add on system")
        else:
            ft_price.set("NT. "+str(ft_price_rate+359))
            add_on_counter3+=1
    ft_choose=Toplevel(root)
    ft_choose.geometry("500x750")
    ft_trailer_B=Button(ft_choose,text="Trailer",width=10,command=ft)
    ft_trailer_B.grid(row=0,column=0,columnspan=10,sticky=W+E)
    ft_description_L=Label(ft_choose,text="Description",font=1000200)
    ft_description_L.grid(row=1,column=0,columnspan=10,sticky=W)
    sframe1=ScrolledFrame(ft_choose,width=400,height=400,bg="white")
    sframe1.grid(row=2,column=0,columnspan=4,sticky=W)
    sframe1.bind_arrow_keys(ft_choose)
    sframe1.bind_scroll_wheel(ft_choose)
    inner_frame=sframe1.display_widget(Frame)
    sframe2=ScrolledFrame(inner_frame,width=400,height=400,bg="white")
    sframe2.grid(row=2,column=0,columnspan=4,sticky=W)
    sframe2.bind_arrow_keys(inner_frame)
    sframe2.bind_scroll_wheel(inner_frame)
    inner_frame2=sframe2.display_widget(Frame)
    ft_description_info=Message(inner_frame2,text=description_text,width=400)
    ft_description_info.grid(row=0,column=0,columnspan=4,sticky=W)

    koi_img=Image.open('Project\Images\Koi_Kindom_pack.jpg')
    koi_img=koi_img.resize((300,400))
    global koi
    koi=ImageTk.PhotoImage(koi_img)
    koi_B=Button(inner_frame,width = 300, height=400,image=koi,command=addOn3)
    koi_L=Label(inner_frame,text="<Fortnite> Koi Kingdom Pack : NT.359")
    koi_B.grid(row=8,column=0,columnspan=8,sticky=W)
    koi_L.grid(row=9,column=0,columnspan=8,sticky=W)
    ft_choose.mainloop()
def pubg_info(): 
    description_text="PUBG: Battlegrounds (previously known as PlayerUnknown's Battlegrounds) is a battle royale game developed by PUBG Studios and published by Krafton. The game, which was inspired by the Japanese film Battle Royale (2000), is based on previous mods created by Brendan PlayerUnknown Greene for other games, and expanded into a standalone game under Greene's creative direction. It is the first game in the PUBG Universe series. The game is played from either a third-person or first-person perspective. In the game, up to one hundred players parachute onto an island where they scavenge for weapons and equipment to kill other players while avoiding getting killed themselves. The available safe area of the game's map decreases in size over time, directing surviving players into an ever tightening space to force encounters. The last surviving player (or team) wins the round. It was first released for Windows via Steam's early access beta program in March 2017, with a full release in December 2017. The game was also released by Microsoft Studios for the Xbox One via its Xbox Game Preview program that same month, and officially released in September 2018. PUBG Mobile, a free-to-play mobile game version for Android and iOS, was released in 2018, in addition to a port for the PlayStation 4. A version for the Stadia streaming platform was released in April 2020, with Xbox Series X/S and PlayStation 5 versions being released in November 2020. The game has been free-to-play for all platforms since January 12, 2022. The game received positive reviews from critics, who found that while the game had some technical flaws, it presented new types of gameplay that could be easily approached by players of any skill level and was highly replayable. The game was credited with popularizing the battle royale genre, with a number of unofficial Chinese clones also being produced following its success. The game received several Game of the Year nominations and set seven Guinness World Records, among many other accolades. PUBG Corporation has run several small tournaments and introduced in-game tools to help with broadcasting the game to spectators, as they wish for it to become a popular esport. It has sold over 75 million copies on personal computers and game consoles, is the best-selling video game on PC and Xbox One, and is the fifth best-selling video game of all time. Currently, the game has accumulated $13 billion in worldwide revenue, including from the more successful mobile version of the game, and it is considered to be one of the highest-grossing video games of all time."   
    def pubg():
        p=Toplevel(root)
        p.geometry("1000x750")
        pu=Label(p)
        pu.pack()
        player4=tkvideo.tkvideo("Project/Images/yt5s.io-PUBG - Stand United_ PGC 2019 Trailer-(480p).mp4",pu,loop=1,size=(1000,750))
        player4.play()
        p.mainloop()
    pubg_choose=Toplevel(root)
    pubg_choose.geometry("500x750")
    pubg_choose["bg"]="#5C564A"
    pubg_trailer_B=Button(pubg_choose,text="Trailer",fg="#F0E5A9",bg="#5C564A",width=10,command=pubg)
    pubg_trailer_B.grid(row=0,column=0,columnspan=10,sticky=W+E)
    pubg_description_L=Label(pubg_choose,text="Description",font=1000200,fg="#F0E5A9",bg="#5C564A")
    pubg_description_L.grid(row=1,column=0,columnspan=10,sticky=W)
    sframe1=ScrolledFrame(pubg_choose,width=400,height=400,bg="#5C564A")
    sframe1.grid(row=2,column=0,columnspan=4,sticky=W)
    sframe1.bind_arrow_keys(pubg_choose)
    sframe1.bind_scroll_wheel(pubg_choose)
    inner_frame=sframe1.display_widget(Frame)
    pubg_description_info=Message(inner_frame,text=description_text,width=400,bg="#5C564A",fg="#F0E5A9")
    pubg_description_info.grid(row=0,column=0,columnspan=4,sticky=W)
    pubg_choose.mainloop()
def choose_genre():
    if theme_Combo.get()=="射擊":
        listVar.set(shooter)
listVar=StringVar()
shooter=["<Call of duty> Mordern Warfare II 2022 ","Rainbow 6 Seige","Fortnite","PUBG Mobile"]
# row=1
title_img=Image.open('Project/Images/290320ed30724fb0aa91d3da057caed0 (1).png')
title_img=title_img.resize((64,64))
title_img=ImageTk.PhotoImage(title_img)
title_label=Label(root,image=title_img,bg="#5C564A")
title_label.grid(row=0,column=0,sticky=W)
theme_Combo=ttk.Combobox(root,value=["射擊","冒險","合作",'恐怖','奇幻','RPG',"動作","多人","沙盒",'解謎'],foreground="#F0E5A9",background="#5C564A")
# theme_Button=Button(root,text="類型: 射擊",font=("Inter",10),fg="#F0E5A9",width=10,height=2,bg="#5C564A")
theme_button=Button(root,text="okay",bg="#5C564A",fg="#F0E5A9",command=choose_genre)
theme_button.grid(row=0,column=2,sticky=E)
theme_Combo.grid(row=0,column=1,sticky=E)
# search_Entry=Entry(root,text="search a game",width=50)
# search_Entry.grid(row=0,column=3,columnspan=3,sticky=E)
listbox=Listbox(root,listvariable=listVar,selectmode="single",height=1,width=30)
listbox.grid(column=3,row=0,columnspan=3,sticky=E)
cart_img=Image.open('Project/Images/istockphoto-1206806317-612x612.png')
cart_img=cart_img.resize((28,30))
cart_img=ImageTk.PhotoImage(cart_img)
cart_Button=Button(root,image=cart_img,bg="#5C564A",command=reciept)
cart_Button.grid(row=0,column=6,sticky=E)
option_Button=Button(root,text="登入/註冊",font=("Inter",10),fg="Black",bg="#F0E5A9",width=8,height=2,command=login_signup_systems)
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
Product_name_label2=Button(root,text="<Rainbow 6> Siege",font=("Inter",10),fg="#F0E5A9",padx=5,bg="#5C564A",command=r6_info)
Product_name_label2.grid(row=3,column=2,columnspan=2,padx=5,sticky=W+E)
Product_name_label3=Button(root,text="<Fortnite> Chapter 4 Season 1",font=("Inter",10),fg="#F0E5A9",bg="#5C564A",command=ft_info)
Product_name_label3.grid(row=3,column=4,columnspan=2,padx=5,sticky=W+E)
Product_name_label4=Button(root,text="<PUBG> Mobile",font=("Inter",10),fg="#F0E5A9",bg="#5C564A",command=pubg_info)
Product_name_label4.grid(row=3,column=6,columnspan=2,padx=5,sticky=W+E)
# row=5
mw_price_rate=2100
r6_price_rate=540
ft_price_rate=0
pubg_price_rate=0
r6_price=StringVar()
r6_price.set("NT."+str(r6_price_rate))
mw_price=StringVar()
mw_price.set("NT."+str(mw_price_rate))
ft_price=StringVar()
ft_price.set("NT."+str(ft_price_rate))
pubg_price=StringVar()
pubg_price.set("NT."+str(pubg_price_rate))

Product_price_label1=Label(root,textvariable=mw_price,font=("Inter",10),fg="#F0E5A9",bg="#5C564A")
Product_price_label2=Label(root,textvariable=r6_price,font=("Inter",10),fg="#F0E5A9",bg="#5C564A")
Product_price_label3=Label(root,textvariable=ft_price,font=("Inter",10),fg="#F0E5A9",bg="#5C564A")
Product_price_label4=Label(root,textvariable=pubg_price,font=("Inter",10),fg="#F0E5A9",bg="#5C564A")
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
# 引入 MIMEText 物件
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

a=input("Please type a url: ")

# 建立 MIMEText 物件
text=MIMEText("Hi, do not get scammed")
# 建立 MIMEImage 物件
image=MIMEImage(Path("C:/Users/halst/Downloads/Dwayne-Johnson-AKA-The-Rock-2019.jpg").read_bytes())
# 創建並設定 MIMEMultipart 物件
content=MIMEMultipart() #建立 MIMEMultipart 物件
content["subject"]="Useless E-mail" #郵件標題
content["from"]="halstonchen1119@gmail.com" #寄件者
content["to"]=a #收件者
content.attach(text) #郵件內容
content.attach(image) #郵件圖片內容
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
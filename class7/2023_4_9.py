from twilio.rest import Client
# 大多數常用操作，只需要用到 Path 類別
from pathlib import Path
import pygsheets

gc=pygsheets.authorize(service_file="C:/Users/halst/Documents/Python_2023_Spring/class7/light-quest-383512-ecae9c4fe19c.json")
sht=gc.open_by_url("https://docs.google.com/spreadsheets/d/1KGAqHO-yo-18AlEgsuihI3O9K5TtSjXV3zgvdHv9ZsQ/edit#gid=0")
# 利用 Index 選取工作表
ws=sht[0]
# 利用名字選取工作列表
# ws=sht.worksheet_by_title("工作表1")
# ws.update_value("A1","I am using python to write something that can just click in and type, which is fun(jk)")
# 讀取表中內容
# value=ws.get_value("A1")
# print("A1's value: "+value)
# A1=ws.cell("A1")
# print("A1's value: "+A1.value)
# # 刪除所有表中內容
# ws.clear()
# 引數傳入你要向的位置，此列指向桌面
# 若沒有傳入引數，預設指向開啟 Python 的位置
# p=Path("./class7/2023_4_9.py")
# # resolve() 找出絕對路徑
# print(p.resolve())
# account_sid = 'ACe3e88393363a9b962c44d0694e39cfd4'
# auth_token = '8ac2e48a0e6d1fbdd913eb8c27a79292'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     from_='+15077086213',
#     body="Never gonna give u up, never gonna let u down, never gonna turn around and hurt u.",
#     to='+886917739664'
# )

# print(message.sid)

ws.update_value("A1","Name")
ws.update_value("B1","Age")
ws.update_value("A2","Amy")
ws.update_value("B2","18")
ws.update_value("A3","Peter")
ws.update_value("B3","15")
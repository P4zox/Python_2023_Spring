from twilio.rest import Client
# 大多數常用操作，只需要用到 Path 類別
from pathlib import Path
import pygsheets
import pandas as pd
import requests

gc=pygsheets.authorize(service_file="C:/Users/halst/Documents/Python_2023_Spring/class7/light-quest-383512-ecae9c4fe19c.json")
sht=gc.open_by_url("https://docs.google.com/spreadsheets/d/1KGAqHO-yo-18AlEgsuihI3O9K5TtSjXV3zgvdHv9ZsQ/edit#gid=0")
# 利用 Index 選取工作表
ws=sht[0]
r=requests.get("https://api.exchangerate-api.com/v4/latest/TWD")
data=r.json()
# print(str(data['rates']["JPY"]))
ws.update_value("A1","國家")
ws.update_value("B1","匯率")
ws.update_value("A2","美國")
ws.update_value("B2",str(data['rates']['USD']))
ws.update_value("A3","日本")
ws.update_value("B3",str(data['rates']['JPY']))
ws.update_value("A4","香港")
ws.update_value("B4",str(data["rates"]['HKD']))


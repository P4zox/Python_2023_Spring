from twilio.rest import Client
# 大多數常用操作，只需要用到 Path 類別
from pathlib import Path
import pygsheets
import pandas as pd

gc=pygsheets.authorize(service_file="C:/Users/halst/Documents/Python_2023_Spring/class7/light-quest-383512-ecae9c4fe19c.json")
sht=gc.open_by_url("https://docs.google.com/spreadsheets/d/1KGAqHO-yo-18AlEgsuihI3O9K5TtSjXV3zgvdHv9ZsQ/edit#gid=0")
# 利用 Index 選取工作表
ws=sht[0]

d={"Customer Name":["non international giant goofy africans","hopkin","orphan with f()btw f means family"],"Weight":[76,44,50]}
df=pd.DataFrame(d)
ws.set_dataframe(df,"A1")
import requests
# 不帶條件
# r=requests.get('url')
# # 有帶條件
# payload={'key':"valuee1","key2":"value2"}
# r=requests.get("url",params=payload)
# r=requests.post("url",data={"key":"value"})

# r=requests.get('https://www.google.com')
# print(r.status_code)

r=requests.get("https://api.exchangerate-api.com/v4/latest/TWD")
data=r.json()
print(str(data['rates']["JPY"]))
import time
from datetime import datetime as dt

hosts_path="hosts"  #r"C:\Users\ERCL\Documents\Python-mega\Course"
redirect="127.0.0.1"
WebsiteList = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("work hours...")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in WebsiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in  WebsiteList):
                    file.write(line)
            file.truncate()
        print("Fun Hours...")
    time.sleep(5)

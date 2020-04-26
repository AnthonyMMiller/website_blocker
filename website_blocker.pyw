import time
from datetime import datetime as dt

#Run as administrator when using host_path. Add to task scheduler to have program automatically run in background on start up
hosts_temp="Add a test file location here"
hosts_path=r" Add host path, for exmaple: C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["crunchyroll.com","www.crunchyroll.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
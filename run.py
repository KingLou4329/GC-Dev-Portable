import os
import shutil
import xml.dom.minidom
from datetime import datetime

import requests

url = 'https://tools.google.com/service/update2'

# Create XML request message for Google Omaha
# https://chromium.googlesource.com/chromium/src.git/+/master/docs/updater/protocol_3_1.md
data = """<?xml version="1.0" encoding="UTF-8"?>
<request protocol="3.1" updater="Omaha" updaterversion="1.3.36.112" shell_version="1.3.36.111"
    installsource="update3web-ondemand" dedup="cr" ismachine="0" domainjoined="0">
    <os platform="win" version="10.0.27749.1000" arch="x64"/>
    <app appid="{8A69D345-D564-463C-AFF1-A69D9E530F96}" ap="x64-dev-multi-chrome" lang="en-us">
        <updatecheck />
    </app>
</request>"""

response = requests.post(url, data=data)

dom = xml.dom.minidom.parseString(response.text)

print(dom.toprettyxml(indent='  '))

url = dom.getElementsByTagName("url")[0].getAttribute("codebase")
name = dom.getElementsByTagName("action")[0].getAttribute("run")

print(url, name)

response = requests.get(url + name)

with open("chrome.7z.exe", "wb") as file:
    file.write(response.content)

os.system('chmod +x ./7zzs')
os.system('./7zzs x chrome.7z.exe')
os.system('./7zzs x chrome.7z')

# 获得Chrome-bin,version.dll,组装到一块就可以分发了
version = '0.0.0.0'
path = 'Chrome-bin'
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        version = i
        break

print(version)
if version == '0.0.0.0':
    exit(1)

# 获得Chrome-bin,version.dll,组装到一块就可以分发了
shutil.move(r'version.dll', 'Chrome-bin')
shutil.move(r'chrome++.ini', 'Chrome-bin')

os.rename(r'Chrome-bin', 'Chrome')
shutil.move(r'Chrome', 'build/release/Chrome')

# 会自动封装为zip
env = os.getenv('GITHUB_ENV')
with open(env, 'a') as f:
    f.write(f'BUILD_NAME=Win64_{version}_{datetime.now().strftime("%Y-%m-%d")}')

# os.system(f'7z.exe a build/release/Win64_{version}_{datetime.now().strftime("%Y-%m-%d")}.7z Chrome')

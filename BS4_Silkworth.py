#!/usr/bin/env python
# coding: utf-8




import requests
from bs4 import BeautifulSoup as bs
import pprint




headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
r = requests.get("https://silkworth.net/alcoholics-anonymous/chapter-1-bills-story/", headers=headers)



soup=bs(r.content, features='xml')

content = soup.select("div p")

soup1=bs(r.content, 'html.parser')
para = soup1.findAll('p')

para = []
for e in content:
    if not e.attrs:
        para.append(e.text)
    
f = open("chap.txt", "w")
f.write(str(para))
f.close()






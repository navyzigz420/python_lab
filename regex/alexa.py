# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 04:37:30 2018

@author: admin
"""
import requests
import re
 

base_url = 'https://www.alexa.com/topsites'
r = requests.get(base_url)
html = r.text

lines = html.split("\n")

myLinkExp = r"<a .*href='(.*)'>(.*)</a>"

for line in lines:
    mygroup = re.search(myLinkExp, line)
    if mygroup:
        mylink = mygroup.group(1)
        mylabel = mygroup.group(2)
        print("{} - {}".format(mylink, mylabel))
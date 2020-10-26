# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:21:02 2020

@author: RICHA
"""

import requests
from bs4 import BeautifulSoup


def get_links(url):
    links=[]
    web=requests.get(url)
    web_text = web.text
    soup = BeautifulSoup(web_text)
    
    for link in soup.find_all('a'):
        links.append(link.get('href'))
        
    for link in links:
        print(link)
        
    print(len(links))

get_links('www.google.com')
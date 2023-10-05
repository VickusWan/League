# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:08:13 2023

@author: Victor
"""

from bs4 import BeautifulSoup
import requests as re

if __name__ == "__main__":
    
    URL = 'https://usedphotopro.com/products/usedcameras/used-slrs/used-film-slrs'
    page = re.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    name = []
    soup_name = soup.find_all('a', class_ = 'product-item-link')
    for n in soup_name:
        name.append(n.text.strip())
        
        condition = []
    soup_cond = soup.find_all('div', class_ = 'condition')
    for cond in soup_cond:
        condition.append(cond.text.replace('\n', ''))
        
    cost = []
    soup_cost = soup.find_all('span', class_ = 'price')
    for c in soup_cost:
        cost.append(c.text)
        
    for i in range(len(name)):
        if 'Minolta' in name[i]:
            print('---------------')
        print(name[i]+', '+condition[i]+', '+cost[i])
        
        if 'Minolta' in name[i]:
            print('---------------')
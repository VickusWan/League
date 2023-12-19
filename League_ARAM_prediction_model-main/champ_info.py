# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:13:53 2020

@author: Victor
"""

import json
import requests

champ = 'https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/champion.json'
re = requests.get(champ)

def champ_info():
    
    champs = {}
    for i in re.json()['data'].values():
        champs[i['id']] = i['key'], i['tags']
        
    return champs

def ChampNumber(name):
    champ_dic = champ_info()
    assert isinstance(name, str), 'Value needs to be a string'    
    assert name in champ_dic.keys(), 'Name is not a League Champion'
    
    return champ_dic[name][0]
    
def ClassOfChamp(name):
    
    champ_dic = champ_info()
    assert isinstance(name, str), 'Value needs to be a string'    
    assert name in champ_dic.keys(), 'Name is not a League Champion'
    
    return champ_dic[name][1]

def get_all_champs():

    champs = {}
    for i in re.json()['data'].values():
        champs[i['name']] = i['tags']
    return champs



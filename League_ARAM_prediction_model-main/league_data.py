# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:37:02 2020

@author: Victor
"""

import champ_info
import requests
import time
#import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

payload = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,en-CA;q=0.8,la;q=0.7",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": ""}

API = os.getenv("API")
    
def fetch(typename, body):
    
    if body == 'AMERICAS':
        init = "https://americas.api.riotgames.com" 
        
    elif body == 'NA1':
        init = "https://na1.api.riotgames.com"
        
    else:
        return 'Not a proper URL'
    
    url = init + typename
    payload['X-Riot-Token'] = API
    re = requests.get(url,headers = payload)    
    if re.status_code == 404:
        return {}
    elif re.status_code == 200:
        time.sleep(1)
        return re.json()

def get_summonerID(puuid):
    typename = '/riot/account/v1/accounts/by-puuid/{puuid}'.format(puuid = puuid)
    body = 'AMERICAS'
    r = fetch(typename, body)
    
    return r['gameName']

def get_puuid(summonerName):
    # Vickus1 puuid = y5cvkCjUQdFfwAUfBdmMFcoCAYsk96GwenHJGiTUUYrygYejQSLLaP3HkrEJVDK_sP8EOnWtJe8lDg
    
    typename = '/lol/summoner/v4/summoners/by-name/{summonerName}'.format(summonerName = summonerName)
    body = 'NA1'
    data = fetch(typename, body)
    return data['puuid']

def get_matchIDs(puuid, start, num_matches):
    
    typename = '/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}'.format(puuid=puuid, start=start, count=num_matches)
    body = 'AMERICAS'
        
    return fetch(typename, body)

def get_participants(matchId):
    
    typename = '/lol/match/v5/matches/{matchId}'.format(matchId = matchId)
    body = 'AMERICAS'
    r = fetch(typename, body)
    
    if not r:
        return []
    else:
        return [i['puuid'] for i in r['info']['participants']]
    

def get_match_data(matchId):
    #'NA1_4013107570',   -> status code 404
    #'NA1_4862739484',   -> status code 200
    typename = '/lol/match/v5/matches/{matchId}'.format(matchId = matchId)
    body = 'AMERICAS'
    
    r = fetch(typename, body)
    if not r:
        return []
    else:
        return r
        
def is_ARAM(matchId):
    typename = '/lol/match/v5/matches/{matchId}'.format(matchId = matchId)
    body = 'AMERICAS'
    data = fetch(typename, body)
    
    if not data:
        return False
    else:
        return data['info']['gameMode'] == 'ARAM'


# def get_full_matchHistory(my_puuid):
    
#     body = 'AMERICAS'
#     match_ids = []
    
#     if len(my_puuid) == 0:
#         return []
    
#     else:
#         start = 0
#         num = 100
    
#         while True:
#             typename = '/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}'.format(puuid = my_puuid, start = start, count = num)
#             data = fetch(typename, body)
            
#             if len(data) == num:
#                 for i in data:
                
#                     if is_ARAM(i) == True:
#                         match_ids.append(i)             
#             else:
#                 break          
#             start += num
    
#     return pd.DataFrame(match_ids)

def match_info(matchId):
    
    typename = '/lol/match/v5/matches/{matchId}'.format(matchId = matchId)
    body = 'AMERICAS'
    
    r = fetch(typename, body)
    player_data = r['info']['participants']
    
    win, loss = [], []
    data = {}
    
    for player in player_data:
        temp = []
        if player['win']:
            temp.append(player['summonerName'])
            temp.append(player['summonerLevel'])
            temp.append(player['puuid'])
            temp.append(player['championName'])
            temp.append(player['championId'])
            win.append(temp)
        else:
            temp.append(player['summonerName'])
            temp.append(player['summonerLevel'])
            temp.append(player['puuid'])
            temp.append(player['championName'])
            temp.append(player['championId'])
            loss.append(temp)
    
    data['win'] = win
    data['loss'] = loss
    return data
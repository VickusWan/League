# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:37:02 2020

@author: Victor
"""

import champ_info
import requests
import time
import pandas as pd
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


def get_full_matchHistory(my_puuid):
    
    body = 'AMERICAS'
    match_ids = []
    
    if len(my_puuid) == 0:
        return []
    
    else:
        start = 0
        num = 100
    
        while True:
            typename = '/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}'.format(puuid = my_puuid, start = start, count = num)
            data = fetch(typename, body)
            
            if len(data) == num:
                for i in data:
                
                    if is_ARAM(i) == True:
                        match_ids.append(i)             
            else:
                break          
            start += num
    
    return pd.DataFrame(match_ids)

def match_info(x):
    
    win = []
    loss = []
    for i in x['teams']:
        if i['win'] == 'Win':
            win.append(i['teamId'])
        else:
            loss.append(i['teamId'])
    
    part = x['participants']
    
    kills_win = 0
    deaths_win = 0
    assists_win = 0
    dmg_win = 0
    dmg_taken_win = 0
    CC_win = 0
    gold_win = 0
    firstTurret_win = 0
    assassin_win = 0
    fighter_win = 0
    mage_win = 0
    marksman_win = 0
    support_win = 0
    tank_win = 0
    
    kills_loss = 0
    deaths_loss = 0
    assists_loss = 0
    dmg_loss = 0
    dmg_taken_loss = 0
    CC_loss = 0
    gold_loss = 0
    firstTurret_loss = 0
    assassin_loss = 0
    fighter_loss = 0
    mage_loss = 0
    marksman_loss = 0
    support_loss = 0
    tank_loss = 0
    
    
    for i in part:
        #name = champ_info.NameOfChamp(i['championId'])
        cl = champ_info.ClassOfChamp(i['championId'])

        if i['teamId'] == win[0]:
            
            kills_win += i['stats']['kills']
            deaths_win += i['stats']['deaths']
            assists_win += i['stats']['assists']
            dmg_win += i['stats']['totalDamageDealt']
            dmg_taken_win += i['stats']['totalDamageTaken']
            CC_win += i['stats']['timeCCingOthers']
            gold_win += i['stats']['goldEarned']
            if i['stats']['firstTowerKill'] == False:
                firstTurret_win += 0
            else:
                firstTurret_win += 1
            
            if cl[0] == 'Assassin':
                assassin_win += 1
            elif cl[0] == 'Fighter':
                fighter_win += 1
            elif cl[0] == 'Mage':
                mage_win += 1
            elif cl[0] == 'Marksman':
                marksman_win += 1
            elif cl[0] == 'Support':
                support_win += 1
            elif cl[0] == 'Tank':
                tank_win += 1
                
            try:
                cl[1]
                if cl[1] == 'Assassin':
                    assassin_win += 1
                elif cl[1] == 'Fighter':
                    fighter_win += 1
                elif cl[1] == 'Mage':
                    mage_win += 1
                elif cl[1] == 'Marksman':
                    marksman_win += 1
                elif cl[1] == 'Support':
                    support_win += 1
                elif cl[1] == 'Tank':
                    tank_win += 1
            except:
                pass
     
        else:
            kills_loss += i['stats']['kills']
            deaths_loss += i['stats']['deaths']
            assists_loss += i['stats']['assists']
            dmg_loss += i['stats']['totalDamageDealt']
            dmg_taken_loss += i['stats']['totalDamageTaken']
            CC_loss += i['stats']['timeCCingOthers']
            gold_loss += i['stats']['goldEarned']
            if i['stats']['firstTowerKill'] == False:
                firstTurret_loss += 0
            else:
                firstTurret_loss += 1
    
            if cl[0] == 'Assassin':
                assassin_loss += 1
            elif cl[0] == 'Fighter':
                fighter_loss += 1
            elif cl[0] == 'Mage':
                mage_loss += 1
            elif cl[0] == 'Marksman':
                marksman_loss += 1
            elif cl[0] == 'Support':
                support_loss += 1
            elif cl[0] == 'Tank':
                tank_loss += 1
                
            try:
                cl[1]
                if cl[1] == 'Assassin':
                    assassin_loss += 1
                elif cl[1] == 'Fighter':
                    fighter_loss += 1
                elif cl[1] == 'Mage':
                    mage_loss += 1
                elif cl[1] == 'Marksman':
                    marksman_loss += 1
                elif cl[1] == 'Support':
                    support_loss += 1
                elif cl[1] == 'Tank':
                    tank_loss += 1
            except:
                pass
            
    win.append(kills_win)
    win.append(deaths_win)
    win.append(assists_win)
    win.append(dmg_win)
    win.append(dmg_taken_win)
    win.append(CC_win)
    win.append(gold_win)
    win.append(firstTurret_win)
    win.append(assassin_win)
    win.append(fighter_win)
    win.append(mage_win)
    win.append(marksman_win)
    win.append(support_win)
    win.append(tank_win)
    
    loss.append(kills_loss)
    loss.append(deaths_loss)
    loss.append(assists_loss)
    loss.append(dmg_loss)
    loss.append(dmg_taken_loss)
    loss.append(CC_loss)
    loss.append(gold_loss)
    loss.append(firstTurret_loss)
    loss.append(assassin_loss)
    loss.append(fighter_loss)
    loss.append(mage_loss)
    loss.append(marksman_loss)
    loss.append(support_loss)
    loss.append(tank_loss)
    
    return win, loss
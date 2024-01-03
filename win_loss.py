# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:12:26 2020

@author: Victor
"""

import time
import sys
sys.path.append('data_extractors')
import league_data
import data_extractors.champ_info as champ_info
import pandas as pd

print(league_data.is_ARAM('wer'))
# name = "/lol/summoner/v4/summoners/by-name/"
# account = "/lol/match/v4/matchlists/by-account/"
# spec = [name, account]
# summoner = "vickus1"
# col = ["matchID", 'total kills', 'total deaths', 'total assists', 'Damage Dealt', "Damage Taken", "Summoner Avg Level", 'Total Gold Earned', '#Assassins', '#Fighters', "#Mages", "#Marksman", "#Supports", "#Tanks", "WIN/LOSS?"]

# puuid = league_data.fetch(name, summoner)['puuid']
# puuid_link = "/lol/match/v5/matches/by-puuid/{puuid}/ids?count=100".format(puuid = puuid)
# #dd = pd.read_csv("Match_history.csv")

# dd = pd.DataFrame(columns = col)

# match_list_ID = league_data.fetch(puuid_link, "")
# champ_list = champ_info.champ_info()

# win = []
# loss = []

# for m in match_list_ID:
#     match_link = "/lol/match/v5/matches/{matchId}".format(matchId = m)
#     match_info = league_data.fetch(match_link, "")
#     info = match_info['info']
    
#     if info['gameMode'] != 'ARAM':
#         continue
    
#     print('ARAM')
#     participant_info = info['participants']
    
#     summonerlvl_win = 0
#     kills_win = 0
#     deaths_win = 0
#     assists_win = 0
#     dmg_win = 0
#     dmg_taken_win = 0
#     gold_win = 0
#     assassin_win = 0
#     fighter_win = 0
#     mage_win = 0
#     marksman_win = 0
#     support_win = 0
#     tank_win = 0
    
#     summonerlvl_loss = 0
#     kills_loss = 0
#     deaths_loss = 0
#     assists_loss = 0
#     dmg_loss = 0
#     dmg_taken_loss = 0
#     gold_loss = 0
#     assassin_loss = 0
#     fighter_loss = 0
#     mage_loss = 0
#     marksman_loss = 0
#     support_loss = 0
#     tank_loss = 0
    
#     for participant in participant_info:
#         if participant['win'] == True:
#             kills_win += participant['kills']
#             deaths_win += participant['deaths']
#             assists_win += participant['assists']
#             dmg_win += participant['totalDamageDealtToChampions']
#             dmg_taken_win += participant['totalDamageTaken']
#             summonerlvl_win += participant['summonerLevel']
#             gold_win += participant['goldEarned']
            
#             champ_class = champ_list[str(participant['championId'])][1]
            
#             if 'Assassin' in champ_class:
#                 assassin_win += 1
#             if 'Fighter' in champ_class:
#                 fighter_win += 1
#             if 'Mage' in champ_class:
#                 mage_win += 1
#             if 'Marksman' in champ_class:
#                 marksman_win += 1
#             if 'Support' in champ_class:
#                 support_win += 1
#             if 'Tank' in champ_class:
#                 tank_win += 1
                
#         else:
#             kills_loss += participant['kills']
#             deaths_loss += participant['deaths']
#             assists_loss += participant['assists']
#             dmg_loss += participant['totalDamageDealtToChampions']
#             dmg_taken_loss += participant['totalDamageTaken']
#             summonerlvl_loss += participant['summonerLevel']
#             gold_loss += participant['goldEarned']
            
#             champ_class = champ_list[str(participant['championId'])][1]
            
#             if 'Assassin' in champ_class:
#                 assassin_loss += 1
#             if 'Fighter' in champ_class:
#                 fighter_loss += 1
#             if 'Mage' in champ_class:
#                 mage_loss += 1
#             if 'Marksman' in champ_class:
#                 marksman_loss += 1
#             if 'Support' in champ_class:
#                 support_loss += 1
#             if 'Tank' in champ_class:
#                 tank_loss += 1
    
#     win.append(m)
#     win.append(kills_win)
#     win.append(deaths_win)
#     win.append(assists_win)
#     win.append(dmg_win)
#     win.append(dmg_taken_win)
#     win.append(summonerlvl_win)
#     win.append(gold_win)
#     win.append(assassin_win)
#     win.append(fighter_win)
#     win.append(mage_win)
#     win.append(marksman_win)
#     win.append(support_win)
#     win.append(tank_win)
#     win.append(1)
    
#     loss.append(m)
#     loss.append(kills_loss)
#     loss.append(deaths_loss)
#     loss.append(assists_loss)
#     loss.append(dmg_loss)
#     loss.append(dmg_taken_loss)
#     loss.append(summonerlvl_loss)
#     loss.append(gold_loss)
#     loss.append(assassin_loss)
#     loss.append(fighter_loss)
#     loss.append(mage_loss)
#     loss.append(marksman_loss)
#     loss.append(support_loss)
#     loss.append(tank_loss)
#     loss.append(0)
    
#     insert = pd.DataFrame(data = [win, loss], columns = col)
#     dd = dd.append(insert, ignore_index = True)
    
#     win.clear()
#     loss.clear()
    

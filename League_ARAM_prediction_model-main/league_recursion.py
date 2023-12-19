# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 22:27:00 2023

@author: Victor
"""

import league_data
import pandas as pd
from tqdm import tqdm
import math, random

def flatten(l):
    
    flat_list = [item for sublist in l for item in sublist]
    
    return flat_list    
    
def reroll(n):
    return math.floor(random.random()*(len(n)-1))


def matchID_recursion(puuid, count, n):
    
    if count == n:
        return
    
    match = league_data.get_matchIDs(puuid, 25) # ['NA1_4743785201']
    match_num = reroll(match)  # finds a random number within that list of match_IDs
        
    # while (int(match[match_num][4:]) < 4014332001):
    #        match_num -= 1
           
    participants = league_data.get_participants(match[match_num]) # ***** this is where it fails
    while not participants:
        match_num -= 1
        participants = league_data.get_participants(match[match_num])
    
    list_participants.append(participants)
    count += 1
    bar.update(1)
    partipant_num = reroll(participants)
    
    while (participants[partipant_num] == "BOT" or len(participants[partipant_num]) < 5):
        partipant_num = reroll(participants)
        
    matchID_recursion(participants[partipant_num],count, n)
    
    return

if __name__ == "__main__":
    # Starting points
    start = 'vickus1'
    starting_puuid = league_data.get_puuid(start)
    df = pd.DataFrame(columns=['matchIDs'])
    list_participants = []
    
    # Progress bar
    n = 500
    bar = tqdm(total=n, position = 0)
    
    matchID_recursion(starting_puuid,0, n)
    flat_list_participants = flatten(list_participants)
    pd.Series(flat_list_participants).to_csv('puuids.csv', mode='a', index=False, header=False)
    
    
    
# puuids = pd.read_csv('puuids.csv', header=None)
# puuids.columns = ['puuids']
# puuids['puuids'].drop_duplicates(inplace=True)
from league_data import match_info, get_matchIDs, is_ARAM
from league_recursion import flatten
import pandas as pd
import csv
from tqdm import tqdm

def get_all_matches():
    df = pd.read_csv('puuids.csv', header=None)
    df.columns = ['puuids']
    df.drop_duplicates(inplace=True)
    puuids = df['puuids'].tolist()

    count = 100
    all_matchIds = []

    start = 25000
    end = 35000

    bar = tqdm(total=(end-start), position = 0)

    for i in range(start, end, 1):
        matchIds = get_matchIDs(puuids[i], 0, count)
        
        if not matchIds:
            continue
        else:
            all_matchIds.extend(matchIds)
        bar.update(1)

    pd.Series(all_matchIds).to_csv('matchIDs.csv', mode='a', index=False, header=False)

def get_ARAM_only():
    df = pd.read_csv('second.csv', header=None)
    df.columns = ['aram']
    df.drop_duplicates(inplace=True)
    matches = df['aram'].tolist()

    currentAramGames = pd.read_csv('../aram_only_data.csv')['gameId'].tolist()
    bar = tqdm(total=len(matches), position = 0)
    for gameId in matches:
        bar.update(1)
        if gameId in currentAramGames:
            continue
        else:
            data = match_info(gameId)
            if not data:
                continue
            else:
                win = flatten(data['win'])
                win.insert(0, 'W')
                win.insert(0, gameId)
                loss = flatten(data['loss'])
                loss.insert(0, 'L')
                loss.insert(0, gameId)

                pd.DataFrame([win, loss]).to_csv('../aram_only_data.csv', mode='a', index=False, header=False)

def get_ARAM_matches():       
    df = pd.read_csv('matchIDs.csv', header=None)
    df.columns = ['matches']
    df.drop_duplicates(inplace=True)
    matches = df['matches'].tolist()

    aram_games = []

    start = 410000
    end = 425000

    bar = tqdm(total=(end-start), position = 0)

    for i in range(start, end, 1):
        isAram = is_ARAM(matches[i])
        bar.update(1)
        if isAram:
            #pd.Series([matches[i]]).to_csv('aram_games.csv', mode='a', index=False, header=False)
            pd.Series([matches[i]]).to_csv('second.csv', mode='a', index=False, header=False)








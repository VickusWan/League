import league_data, league_recursion
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
        matchIds = league_data.get_matchIDs(puuids[i], 0, count)
        
        if not matchIds:
            continue
        else:
            all_matchIds.extend(matchIds)
        bar.update(1)

    pd.Series(all_matchIds).to_csv('matchIDs.csv', mode='a', index=False, header=False)

#def get_ARAM_only():
df = pd.read_csv('aram_games.csv', header=None)
df.columns = ['aram']
df.drop_duplicates(inplace=True)
matches = df['aram'].tolist()

currentAramGames = pd.read_csv('aram_only_data.csv')['gameId'].tolist()
bar = tqdm(total=len(matches), position = 0)
for gameId in matches:
    bar.update(1)
    if gameId in currentAramGames:
        continue
    else:
        data = league_data.match_info(gameId)
        if not data:
            continue
        else:
            win = league_recursion.flatten(data['win'])
            win.insert(0, 'W')
            win.insert(0, gameId)
            loss = league_recursion.flatten(data['loss'])
            loss.insert(0, 'L')
            loss.insert(0, gameId)

            pd.DataFrame([win, loss]).to_csv('aram_only_data.csv', mode='a', index=False, header=False)








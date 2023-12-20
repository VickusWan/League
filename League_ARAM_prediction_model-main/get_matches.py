import league_data
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

    start = 2000
    end = 15000

    bar = tqdm(total=(end-start), position = 0)

    for i in range(start, end, 1):
        matchIds = league_data.get_matchIDs(puuids[i], 0, count)
        
        if not matchIds:
            continue
        else:
            all_matchIds.extend(matchIds)
        bar.update(1)

    pd.Series(all_matchIds).to_csv('matchIDs.csv', mode='a', index=False, header=False)


df = pd.read_csv('matchIDs.csv', header=None)
df.columns = ['matches']
df.drop_duplicates(inplace=True)
matches = df['matches'].tolist()

count = 100
aram_games = []

start = 15000
end = 20000

bar = tqdm(total=(end-start), position = 0)

for i in range(start, end, 1):
    isAram = league_data.is_ARAM(matches[i])
    bar.update(1)
    if isAram:
        aram_games.append(matches[i])
    else:
        continue
    

pd.Series(aram_games).to_csv('aram_games.csv', mode='a', index=False, header=False)






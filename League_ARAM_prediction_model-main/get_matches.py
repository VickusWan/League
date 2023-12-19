import league_data
import pandas as pd
from tqdm import tqdm

df = pd.read_csv('puuids.csv', header=None)
df.columns = ['puuids']
df.drop_duplicates(inplace=True)
puuids = df['puuids'].tolist()

count = 100
all_matchIds = []

start = 200
end = 400

bar = tqdm(total=(end-start), position = 0)

for i in range(start, end, 1):
    matchIds = league_data.get_matchIDs(puuids[i], 0, count)
    all_matchIds.extend(matchIds)
    bar.update(1)

pd.Series(all_matchIds).to_csv('matchIDs.csv', mode='a', index=False, header=False)

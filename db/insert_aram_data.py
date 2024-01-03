from dotenv import load_dotenv
import os
import psycopg2
from urllib.parse import urlparse
import csv
import json
import pandas as pd
from tqdm import tqdm

load_dotenv()
database_url = os.getenv("DATABASE_URL")

url_parts = urlparse(database_url)
db_params = {
    'user': url_parts.username,
    'password': url_parts.password,
    'host': url_parts.hostname,
    'port': url_parts.port,
    'database': url_parts.path[1:],  # Remove the leading '/'
}

def return_insert(gameId, data):
    temp_win, temp_loss = [], []
    temp_win.append(gameId)
    temp_loss.append(gameId)
    for key, value in data.items():
        temp = []
        temp.append(key)
        for player in value:
            temp.append(player[2])
            temp.append(player[1])
            temp.append(player[3])
            temp.append(player[4])
            
            # ['summonerName',
            #  summonerLevel,
            #  'puuid',
            #  'champName',
            #  champId]
        
        if key == 'win':
            temp_win.extend(temp)
        else:
            temp_loss.extend(temp)
    return (temp_win, temp_loss)

df = pd.read_csv('aram_only_data.csv')

bar = tqdm(total=df.shape[0], position = 0)

with psycopg2.connect(**db_params) as connection:
    with connection.cursor() as cursor:
        for index, row in df.iterrows():         

            insert_query = f'''INSERT INTO aram_data 
            (gameid, game_result, puuid_p1, level_p1, champ_name_p1, champ_id_p1,
            puuid_p2, level_p2, champ_name_p2, champ_id_p2,
            puuid_p3, level_p3, champ_name_p3, champ_id_p3,
            puuid_p4, level_p4, champ_name_p4, champ_id_p4,
            puuid_p5, level_p5, champ_name_p5, champ_id_p5) 
            VALUES ('{row.iloc[0]}', '{row.iloc[1]}', '{row.iloc[2]}', '{row.iloc[3]}', '{row.iloc[4]}', '{row.iloc[5]}', '{row.iloc[6]}', '{row.iloc[7]}', '{row.iloc[8]}',
            '{row.iloc[9]}','{row.iloc[10]}','{row.iloc[11]}','{row.iloc[12]}','{row.iloc[13]}','{row.iloc[14]}','{row.iloc[15]}','{row.iloc[16]}','{row.iloc[17]}','{row.iloc[18]}',
            '{row.iloc[19]}','{row.iloc[20]}','{row.iloc[21]}');'''
            cursor.execute(insert_query)
            bar.update(1)

    connection.commit()
print("Values inserted successfully.")



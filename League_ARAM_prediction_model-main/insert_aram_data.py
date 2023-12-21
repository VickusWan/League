from dotenv import load_dotenv
import os
import psycopg2
from urllib.parse import urlparse
import csv
import champ_info
import json
import pandas as pd
import league_data
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

df = pd.read_csv('/mnt/c/Users/victo/OneDrive/Desktop/League/League_ARAM_prediction_model-main/aram_games.csv', header=None)
bar = tqdm(total=df.shape[0], position = 0)

with psycopg2.connect(**db_params) as connection:
    with connection.cursor() as cursor:
        for row in df[0]:
            aram_data = league_data.match_info(row)
            for data in return_insert(row, aram_data):            

                insert_query = f'''INSERT INTO aram_data 
                (gameid, condition, puuid_p1, level_p1, champ_name_p1, champ_id_p1,
                puuid_p2, level_p2, champ_name_p2, champ_id_p2,
                puuid_p3, level_p3, champ_name_p3, champ_id_p3,
                puuid_p4, level_p4, champ_name_p4, champ_id_p4,
                puuid_p5, level_p5, champ_name_p5, champ_id_p5) 
                VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}', '{data[7]}', '{data[8]}',
                '{data[9]}','{data[10]}','{data[11]}','{data[12]}','{data[13]}','{data[14]}','{data[15]}','{data[16]}','{data[17]}','{data[18]}',
                '{data[19]}','{data[20]}','{data[21]}');'''
                cursor.execute(insert_query)
                bar.update(1)

    connection.commit()
print("Values inserted successfully.")

            
            

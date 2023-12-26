from dotenv import load_dotenv
import os
import psycopg2
from urllib.parse import urlparse
import csv
import data_extractors.champ_info as champ_info
import json

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

with psycopg2.connect(**db_params) as connection:
    with connection.cursor() as cursor:
        for key, value in champ_info.get_all_champs().items():
            champ = value['name'].replace("'", "''")
            title = value['title'].replace("'", "''")
            image = value['image'].replace("'", "''")
            class_data = json.dumps(value['class']).replace("'", "''")

            insert_query = f'''INSERT INTO champinfo 
            (champ_key, champ_name, title, difficulty, image, class) 
            VALUES ('{value['key']}', '{champ}', '{title}', {value['difficulty']}, '{image}', '{class_data}');'''
            cursor.execute(insert_query)

    connection.commit()
print("Values inserted successfully.")

with psycopg2.connect(**db_params) as connection:
    with connection.cursor() as cursor:
        with open('champ_pokes.csv', newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            next(filereader)
            for row in filereader:
                words = row[0].split(',')

                insert_query = f'''INSERT INTO poke 
                (champ_name, q, w, e, r, total, hard_cc) 
                VALUES ('{words[0]}', '{int(words[1])}', '{int(words[2])}', {int(words[3])}, '{int(words[4])}', '{int(words[5])}', '{int(words[6])}');'''
                cursor.execute(insert_query)

    connection.commit()
print("Values inserted successfully.")
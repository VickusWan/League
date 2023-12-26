from dotenv import load_dotenv
import os
import psycopg2
from urllib.parse import urlparse
import pandas as pd

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

def get_training_data():
    connection = psycopg2.connect(**db_params)

    select_query = f'''
    SELECT game_result,
    ad.level_p1, ad.champ_name_p1, info1.class, poke1.total, poke1.hard_cc,
    ad.level_p2, ad.champ_name_p2, info2.class, poke2.total, poke2.hard_cc,
    ad.level_p3, ad.champ_name_p3, info3.class, poke3.total, poke3.hard_cc,
    ad.level_p4, ad.champ_name_p4, info4.class, poke4.total, poke4.hard_cc,
    ad.level_p5, ad.champ_name_p5, info5.class, poke5.total, poke5.hard_cc
    FROM aram_data as ad
    LEFT JOIN champinfo as info1 ON ad.champ_id_p1 = info1.champ_key
    LEFT JOIN poke as poke1 ON ad.champ_name_p1 = poke1.champ_name 
    LEFT JOIN champinfo as info2 ON ad.champ_id_p2 = info2.champ_key
    LEFT JOIN poke as poke2 ON ad.champ_name_p2 = poke2.champ_name
    LEFT JOIN champinfo as info3 ON ad.champ_id_p3 = info3.champ_key
    LEFT JOIN poke as poke3 ON ad.champ_name_p3 = poke3.champ_name
    LEFT JOIN champinfo as info4 ON ad.champ_id_p4 = info4.champ_key
    LEFT JOIN poke as poke4 ON ad.champ_name_p4 = poke4.champ_name
    LEFT JOIN champinfo as info5 ON ad.champ_id_p5 = info5.champ_key
    LEFT JOIN poke as poke5 ON ad.champ_name_p5 = poke5.champ_name;
    '''

    df = pd.read_sql_query(select_query, connection)
    connection.close()
    return df

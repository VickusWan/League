from dotenv import load_dotenv
import os
import psycopg2
from urllib.parse import urlparse

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

create_table_champ_info = f'''
    CREATE TABLE IF NOT EXISTS {'champInfo'} (
        champ_key SERIAL PRIMARY KEY,
        champ_name VARCHAR(255),
        title VARCHAR(255),
        difficulty INT,
        image VARCHAR(255),
        class VARCHAR(255)
    );
'''


create_table_poke = f'''
    CREATE TABLE IF NOT EXISTS {'poke'} (
        id SERIAL PRIMARY KEY,
        champ_name VARCHAR(255),
        Q INT,
        W INT,
        E INT,
        R INT,
        total INT,
        hard_CC INT
    );
'''

try:
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            cursor.execute(create_table_champ_info)
            cursor.execute(create_table_poke)

        connection.commit()
        print("Tables created successfully (if it did not exist).")

except Exception as e:
    print(f"Error: {e}")


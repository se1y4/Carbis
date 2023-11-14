from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import sqlite3 as sq
import os

with sq.connect("settings.db") as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS settings (
                    id INTEGER PRIMARY KEY,
                    base_url TEXT,
                    api_key TEXT,
                    language TEXT
                  )''')

def save_settings(base_url, api_key, language):
    cursor.execute("SELECT count(*) FROM settings")
    data = cursor.fetchone()
    if data[0] == 0:
        cursor.execute("INSERT INTO settings (base_url, api_key, language) VALUES (?, ?, ?)", (base_url, api_key, language))
    else:
        cursor.execute("UPDATE settings SET base_url=?, api_key=?, language=?", (base_url, api_key, language))

    connection.commit()

url = "https://dadata.ru/"
api_key = " "
default_language = "en"

save_settings(url, api_key, default_language)
import sqlite3 as sq

with sq.connect("settings.db") as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS settings (
                    id INTEGER PRIMARY KEY,
                    base_url TEXT,
                    api_key TEXT,
                    language TEXT
                  )''')



def save_settings( api_key, language = "ru"):
    cursor.execute("SELECT count(*) FROM settings")
    data = cursor.fetchone()
    if data[0] == 0:
        cursor.execute("INSERT INTO settings (base_url, api_key, language) VALUES (?, ?, ?)", ("https://dadata.ru/", api_key, language))
    else:
        cursor.execute("UPDATE settings SET base_url=?, api_key=?, language=?", ("https://dadata.ru/", api_key, language))

    connection.commit()

def import_language(user_API):
    connection = sq.connect("settings.db")
    cursor = connection.cursor()
    cursor.execute("SELECT language FROM settings WHERE api_key=?", (user_API,))
    language = cursor.fetchone()
    language = language[0]
    connection.close()
    return language

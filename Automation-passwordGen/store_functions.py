import random
import sqlite3
import webbrowser
from public_functions import db_path



def generate_password():
    password = ""
    characters = [chr(i) for i in range(34, 127)]
    lenght = random.randint(12, 20)
    for i in range(lenght):
        char_to_add = random.choice(characters)
        password = password + char_to_add
    return password


def store_input(entry_url, entry_description):
    url = entry_url.get()
    description = entry_description.get()
    clear_entry(entry_url, entry_description)
    store_in_database(url, description)


    # chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

def clear_entry(*entries):
    for entry in entries:
        entry.config(text = "")

def store_in_database(url, description):
    password = generate_password()
    with sqlite3.connect(db_path) as conn:
        command_insert = "INSERT INTO passwordDB VALUES(?, ?, ?)"
        
        cursor = conn.cursor()
        cursor.execute("SELECT URL FROM passwordDB ORDER BY URL DESC")
        data = cursor.fetchall()
        results = [row[0] for row in data]
        for result in results:
            if result == url:
                command_delete = f"DELETE FROM passwordDB WHERE URL = '{result}'"
                conn.execute(command_delete)
                print("executed")
        conn.execute(command_insert, (url, password, description))


def clear_db():
    with sqlite3.connect(db_path) as conn:
        command_delete = "DELETE FROM passwordDB"
        conn.execute(command_delete)
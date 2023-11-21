import sqlite3
from public_functions import db_path, correct_word


def retrieve_password(entry_url, entry_desc, lbl_retrieve_result):
    desc = entry_desc.get()
    url =  entry_url.get()
    if desc == "":
        password = url_search(url)
        display_password(lbl_retrieve_result, password)
    elif url == "":
        password = desc_search(desc)
        display_password(lbl_retrieve_result, password)
    else:
        password_url = url_search(url)
        password_desc = desc_search(desc)

        if password_url:
            display_password(lbl_retrieve_result, password_url)
        elif password_desc:
            display_password(lbl_retrieve_result, password_desc)
        else:
            display_password(lbl_retrieve_result, password)


def url_search(url):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT password FROM passwordDB WHERE URL = '{url}'")
        results = cursor.fetchall()
        if len(results) == 0:
            return False
        else:
            return results[0][0]

def desc_search(user_input):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Get best description
        cursor.execute("SELECT description FROM passwordDB")
        descriptions = cursor.fetchall()
        desc = correct_word(user_input, descriptions[0])
        if desc:
            cursor.execute(f"SELECT password FROM passwordDB WHERE description = '{desc}'")
            results = cursor.fetchall()
            if len(results) == 0:
                return False
            else:
                return results[0][0]
            


def display_password(label, password):
    if not password:
        label.config(text = "No password found.")
    else:
        label.config(text = "Password: " + password)

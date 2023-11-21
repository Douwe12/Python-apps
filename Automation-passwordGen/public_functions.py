import os
import sqlite3


def get_path_current_dir(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    return os.path.join(script_dir, file_name)

def correct_word(string, words):
    string = string.lower()
    common_dict = {}
    for word in words:
        total_common = 0
        for index, letter in enumerate(word):                      
            try:
                if index == 0:
                    if string[index] in letter[index: index + 1]:               
                        total_common +=1 
                elif string[index] in word[index -1: index + 1]:
                    total_common += 1
            except IndexError:
                break
        common_dict[word.lower()] = total_common
    max_value = max(common_dict.values())
    highest_common_words = [key for key, value in common_dict.items() if value == max_value]                          
    corrected_word = min(highest_common_words, key = lambda word: len(word))
    if len(corrected_word) > 5:
        if len(corrected_word) - 5 > max_value:
            return False
    return corrected_word

# initialize shared variables
db_path = get_path_current_dir("url_password_db.sqlite3")
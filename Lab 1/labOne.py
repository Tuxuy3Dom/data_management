import json
import difflib
from difflib import get_close_matches
from difflib import SequenceMatcher

# open json file
with open('data.json', encoding = 'utf-8') as dataStudent:
    data = json.load(dataStudent)

# fetching the string specified by the user and convert uppercase letters to lowercase
key_word = input("Podaj wyraz: ").lower()

# function check keys in json file
def check_key_words(key_word):
    if key_word in data.keys():
        print(f'Podany wyraz to: "{key_word}"', f'\nWynik: {data[key_word]}')
    else:
        print(f'Podany wyraz = "{key_word}" nie istnieje w pliku. Sprawdź ponownie.')


keys = list(data.keys())

def find_best_key(input_key, data_keys):
    
    best_match = None
    best_ratio = 0.5

    for key in data_keys:
        ratio = difflib.SequenceMatcher(None, input_key, key).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = key

    if best_match is None:
        return None
    else: 
        print(f'Czy chciałeś podać {best_match}?')
        find_accepted = input("Podaj T lub N: ").upper()
        if find_accepted == 'T':
            return print(f'Wynik podanego wyrazu: {data[best_match]}')
        else:
            return print(f'Wyraz = "{input_key}" nie istnieje w pliku. Sprawdź ponownie.')
    
def check_key_word(key_word):
    result = data.get(key_word.lower(), None)
    if result is not None:
        if isinstance(result, list):
            for r in result:
                print(r)
        else:
            print(result)
    else:
        close_matches = get_close_matches(key_word, data.keys(), n=3, cutoff=0.6)
        if len(close_matches) > 0:
            suggestion = close_matches[0]
            confirm = input(f"Czy miałeś na myśli '{suggestion}'? [Tak/Nie] ")
            if confirm.lower() == "tak":
                if isinstance(data[suggestion], list):
                    for r in data[suggestion]:
                        print(r)
                else:
                    print(data[suggestion])
            else:
                print(f'Wyraz = "{key_word}" nie istnieje w pliku. Sprawdź ponownie.')
        else:
            print("Brak dopasowania dla podanego wyrazu.")

# view file content
print(check_key_words(key_word))
print(find_best_key(key_word, keys))
print(check_key_word(key_word))
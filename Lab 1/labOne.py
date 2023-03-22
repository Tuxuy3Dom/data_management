import json
import difflib
from difflib import get_close_matches
from difflib import SequenceMatcher

# open json file
with open('dataUniversity.json', encoding='utf-8') as dataStudent:
    data = json.load(dataStudent)

# Optimization code in function check_input_key
def array_form_items(result):
    if isinstance(result, list):
        for r in result:
            print(r)
    else:
        print(result)

# Find close matches using the get_close_matches function from difflib
def find_best_key(input_key):
    close_matches = get_close_matches(input_key, data.keys(), n=3, cutoff=0.6)[0]
    if len(close_matches) > 0:
        confirm = input(f"Czy miałeś na myśli '{close_matches}'? [Tak/Nie] ")
        if confirm.lower() == "tak":
            return array_form_items(data[close_matches])
        elif confirm.lower() == "nie":
            return print(f'Napewno nie ma danego słowa "{close_matches}"?')
        else:
            if input_key.upper() in data:
                return array_form_items(data[input_key.upper()])
            else:
                return print(f'Wyraz = "{input_key}" nie istnieje w pliku. Sprawdź ponownie.')
    else:
        if input_key.upper() in data:
            return array_form_items(data[input_key.upper()])
        else:
            proper_nouns = [k for k in data.keys() if k[0].isupper()]
            matches = get_close_matches(input_key, proper_nouns, n=3, cutoff=0.6)[0]
            if len(matches) > 0:
                confirm = input(
                    f"Czy miałeś na myśli '{matches}'? [Tak/Nie] ")
                if confirm.lower() == "tak":
                    return array_form_items(data[matches])
                elif confirm.lower() == "nie":
                    return print(f'Napewno nie ma danego słowa "{matches}"?')
                else:
                    return print(
                        f'Wyraz = "{input_key}" nie istnieje w pliku. Sprawdź ponownie.')
            else:
                return print("Brak dopasowania dla podanego wyrazu. Sprawdź ponownie.")

# function check keys in json file
def check_input_key(input_key):
    result = data.get(input_key, None)
    # Check if the input is an acronym (all caps)
    if input_key.isupper():
        # result = data.get(input_key, None)
        if result is not None:
            return array_form_items(result)
        else:
            return find_best_key(input_key)
    else:
        # Check if the input starts with a capital letter (possible proper noun)
        if input_key[0].isupper():
            # result = data.get(input_key, None)
            if result is not None:
                return array_form_items(result)
            else:
                # Check if the input is an acronym in the form "ABC"
                if len(input_key) <= 3 and input_key.isalpha():
                    result = data.get(input_key.upper(), None)
                    if result is not None:
                        return array_form_items(result)
                    else:
                        return find_best_key(input_key)
                else:
                    # Convert the input to lowercase
                    input_key = input_key.lower()

                    # Try to find a match for the lowercase version of the input
                    result = data.get(input_key, None)
                    if result is not None:
                        return array_form_items(result)
                    else:
                        # If no match was found for the lowercase version, try the original input
                        result = data.get(input_key.title(), None)
                        if result is not None:
                            return array_form_items(result)
                        else:
                            # Find close matches using the get_close_matches function from difflib
                            return find_best_key(input_key)
        else:
            if input_key.lower():
                # result = data.get(input_key, None)
                if result is not None:
                    return array_form_items(result)
                else:
                    return find_best_key(input_key)
            else:
                return print("Brak dopasowania wyrazu. Sprawdź ponownie.")

# Input keys in file ison
input_key = input("Podaj wyraz: ")

# view file database
result = check_input_key(input_key)
if isinstance(result, str):
    print(result)
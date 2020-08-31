# -*- coding: utf-8 -*-

import json
import random


# Give a Json file and return a list
def read_values_from_json(file, key):
    # create a new empty list
    values = []

    # open a json file with my objects
    with open(file) as f:
        # load all the data contained in this file
        data = json.load(f)

        # data = entries
        for entry in data:
            # add each item in my list
            values.append(entry[key])
    return values


# Give a json and return a list
def clean_strings(sentences):
    cleaned = []

    # Store quotes on list,
    # Create an empty list and add each
    # sentence one by one
    for sentence in sentences:
        # Clean quotes from whitespace and so on
        clean_sentence = sentence.strip()

        # don't use extend as it adds each letter
        # one by one
        cleaned.append(clean_sentence)
    return cleaned


# Return a random item in a list
def random_item_in(object_list):
    random_number = random.randint(0, len(object_list) - 1)
    return object_list[random_number]


# Return a random value from a json file
def random_values(path, key):
    values = read_values_from_json(path, key)
    clean_values = clean_strings(values)
    return random_item_in(clean_values)


# random quotes
def random_quote():
    return random_values('data/quotes.json', 'quote')


# random charateres from Wikipedia
def random_character():
    return random_values('data/characters.json', 'character')


# Interaction : print a random sentence
def print_random_sentence():
    rquote = random_quote()
    rchar = random_character()
    print('>>> {} a dit : {}'.format(rquote, rchar))


def main():
    while True:
        print_random_sentence()
        message = (
            'Voulez-vous voir une autre citation ?'
            ' Pour sortir du programme, tapez [Q].'
        )
        response = input(message).upper()
        if response == 'Q' or response == 'q':
            break
            # This will stop the loop !


if __name__ == '__main__':
    main()

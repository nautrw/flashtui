import json
from itertools import pairwise
from typing import List


def create_config(path: str) -> None:
    '''
    Creates the configuration file for the program
    '''

    with open(path, 'w+') as file:
        if not file.read():
            file.write('{}')


def read_config(path: str) -> dict:
    '''
    Returns the configuration data in the configuration file
    '''

    with open(path, 'r') as file:
        file = file.read()
        return json.loads(file)


def read_deck_from_text(format: str, text: str) -> List[tuple]:
    separator = format.replace('{term}', '').replace('{definition}', '')
    split_list = text.split(separator)
    deck_pairs = pairwise(split_list)
    return list(deck_pairs)

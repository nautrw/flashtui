import json
import random
from itertools import pairwise
from typing import List


def create_config(path: str) -> None:
    """
    Creates the configuration file for the program
    """

    with open(path, "w+") as file:
        if not file.read():
            file.write('{"decks":{}}')


def read_config(path: str) -> dict:
    """
    Returns the configuration data in the configuration file
    """

    with open(path, "r") as file:
        return json.load(file)


def read_deck_from_text(format: str, text: str) -> List[List]:
    lines = text.strip().splitlines()

    separator = format.replace("{term}", "").replace("{definition}", "")

    deck_pairs = [line.split(separator) for line in lines]

    return deck_pairs


def add_deck_to_config(config_path: str, name: str, pairs: List[List]) -> None:
    config = read_config(config_path)

    with open(config_path, "w") as file:
        config["decks"][name] = [[term, definition]
                                 for term, definition in pairs]

        json.dump(config, file)


def make_practice(config_path: str, deck_name: str, shuffle: bool, reverse_deck: bool) -> List:
    config = read_config(config_path)
    questions_list = config['decks'][deck_name]

    if shuffle:
        random.shuffle(questions_list)

    print(questions_list)

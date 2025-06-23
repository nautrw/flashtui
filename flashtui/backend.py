import json
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


def read_deck_from_text(format: str, text: str) -> List[tuple]:
    separator = format.replace("{term}", "").replace("{definition}", "")
    split_list = text.split(separator)
    deck_pairs = pairwise(split_list)
    return list(deck_pairs)


def add_deck_to_config(config_path: str, name: str, pairs: List[tuple]) -> None:
    config = read_config(config_path)

    with open(config_path, "w") as file:
        config["decks"][name] = [{term.replace('\n', ''): definition.replace('\n', '')}
                                 for term, definition in pairs]

        json.dump(config, file)

import json


def create_config(path: str) -> None:
    '''
    Creates the configuration file for the program
    '''

    with open(path, 'w+') as file:
        if not file.read():
            file.write('{}')


def read_config(path: str) -> None:
    '''
    Returns the configuration data in the configuration file
    '''

    with open(path, 'r') as file:
        file = file.read()
        return json.loads(file)

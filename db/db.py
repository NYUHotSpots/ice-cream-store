"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import os

DB_Path = os.environ["DB_Path"]
ICE_CREAM_DB = f"{DB_Path}/db/ice_cream.json"


def get_ice_cream():
    """
    A function to return all chat rooms.
    """
    print(DB_Path)
    print(ICE_CREAM_DB)
    try:
        with open(ICE_CREAM_DB[1:]) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None

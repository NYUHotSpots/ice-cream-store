"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import os

DB_Path = os.environ["DB_Path"]
TEST_MODE = os.environ.get("TEST_MODE", 0)

if TEST_MODE:
    DB_DIR = f"{DB_Path}/db/test_dbs"
else:
    DB_DIR = f"{DB_Path}/db"


ICE_CREAM_DB = f"{DB_DIR}/ice_cream.json"
USERS_DB = f"{DB_DIR}/users.json"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


def get_ice_cream():
    """
    A function to return all ice cream flavors and price
    """
    try:
        with open(ICE_CREAM_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None


def add_ice_cream(new_flavor, price=0):
    """
    Add a flavor to the ice cream database
    Until we use a real DB, we might have race condition
    """
    flavors = get_ice_cream()
    if flavors is None:
        return NOT_FOUND
    elif new_flavor in flavors:
        return DUPLICATE
    else:
        flavors[new_flavor] = {"price": price}
        write_ice_cream(flavors)
        return OK


def write_ice_cream(flavors):
    """
    Write out the in memory ice cream list in proper DB format
    """
    with open(ICE_CREAM_DB, 'w') as f:
        json.dump(flavors, f, indent=4)


def get_users():
    """
    A function to return a dictionary of all users.
    """
    try:
        with open(USERS_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print("Users db not found.")
        return None


def add_user(username, type="BUYER"):
    """
    Add a user to the user database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    users = get_users()
    if users is None:
        return NOT_FOUND
    elif username in users:
        return DUPLICATE
    else:
        users[username] = {"type": type}
        write_users(users)
        return OK


def write_users(users):
    pass

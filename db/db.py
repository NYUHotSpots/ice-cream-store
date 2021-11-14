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

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


def get_ice_cream():
    """
    A function to return all ice cream flavors and price
    """
    print(ICE_CREAM_DB)
    try:
        with open(ICE_CREAM_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None


def get_users():
    """
    A function to get all users
    """
    return {"user1", "user2"}


# def add_user(username):
#     """
#     Add a user to the user database.
#     Until we are using a real DB, we have a potential
#     race condition here.
#     """
#     users = get_users()
#     if users is None:
#         return NOT_FOUND
#     elif username in users:
#         return DUPLICATE
#     else:
#         users[username] = {"num_users": 0}
#         write_users(users)
#         return OK

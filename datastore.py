import os
import json
from threading import Timer


def datastore(filepath=os.getcwd()):
    if not os.path.exists(filepath):
        print("The Entered Directory Doesn't exists")
        return

    filename = "key_value_data_store.dat"
    full_path = os.path.join(filepath, filename)

    # If the data store is not existing already in the path, we create a store in the path
    if not os.path.isfile(full_path):
        open(full_path, "w")


def create(key, value, timeout=0):
    # 1GB limit checker
    if os.path.getsize('key_value_data_store.dat') > (1024 * 1024 * 1024):
        print("File Size Limit Reached - Cannot Create more")
        return

    if len(key) > 32:
        print("Invalid Key")
        return

    try:
        dic = json.load(open('key_value_data_store.dat'))
    except:
        # If it is an empty data store
        dic = {}

    if key in dic:
        print("Key already Exists")
        return

    dic.update({key: value})
    json.dump(dic, open('key_value_data_store.dat', 'w'))
    print("Key added Successfully")

    if timeout > 0:
        Timer(timeout, delete, [key]).start()
        # After the given time-to-live seconds, the key will be deleted


def read(key):
    # reading from the datastore and assigning as a dictionary
    try:
        data_store = json.load(open('key_value_data_store.dat'))
    except:
        return "Data Store Empty"

    return data_store[key] if key in data_store else "Key not Present"


def delete(key):
    try:
        dic = json.load(open('key_value_data_store.dat'))
    except:
        return "Data Store Empty"

    if key in dic:
        del dic[key]
    else:
        print("Key not Present")

    json.dump(dic, open('key_value_data_store.dat', 'w'))



#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if key is a string
    if not isinstance(key, str):
        print("Error: Key must be a string.")
        return

    # Delete the key from the dictionary if it exists
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

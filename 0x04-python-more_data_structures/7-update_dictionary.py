#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not isinstance(key, str):
        print("Error: Key must be a string.")
        return

    # Add or replace key/value in the dictionary
    a_dictionary[key] = value

    # Return the updated dictionary
    return a_dictionary

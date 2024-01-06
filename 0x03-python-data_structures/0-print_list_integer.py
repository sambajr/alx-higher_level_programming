#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints each integer from the given list on a separate line.

    Parameters:
    - my_list (list): The list containing integers to be printed.
    """
    for i in my_list:
        if type(i) is int:
            print("{}".format(i))

#!/usr/bin/python3
def no_c(my_string):
    modif_str = ""
    for i in my_string:
        if i.lower() != 'c':
            modif_str += i
    return modif_str

#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
        return result
    except ZeroDivisionError:
        return None
    finally:
        if 'result' not in locals():
            print("Inside result: None")

#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Extract arguments from the command line
    arguments = sys.argv[1:]

    # Cast arguments to integers and calculate the sum
    result = sum(int(arg) for arg in arguments)

    # Print the result followed by a new line
    print(result)

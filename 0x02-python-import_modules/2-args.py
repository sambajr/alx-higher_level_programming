#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name

    # Print the number of arguments
    if num_args == 1:
        print(f"{num_args} argument", end="")
    else:
        print(f"{num_args} arguments", end="")

    if num_args == 0:
        print(".")  # If no arguments, print a dot and a new line
    else:
        print(":")  # If at least one argument, print a colon and a new line

        # Print one line per argument
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")

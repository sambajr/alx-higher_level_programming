#!/usr/bin/python3
# Import the required function
# Import the required function
from add_0 import add


def main():
    # Define the variables
    a, b = 1, 2

    # Compute the sum
    sum_ab = add(a, b)

    # Print the result in the required format
    print(f"{a} + {b} = {sum_ab}")


# Ensure the main function is only executed when this script is run directly
if __name__ == "__main__":
    main()

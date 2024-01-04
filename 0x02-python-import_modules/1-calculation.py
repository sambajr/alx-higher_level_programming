#!/usr/bin/python3


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # Print the result of addition
    print(f"{a} + {b} = {add(a, b)}")

    # Print the result of subtraction
    print(f"{a} - {b} = {sub(a, b)}")

    # Print the result of multiplication
    print(f"{a} * {b} = {mul(a, b)}")

    # Print the result of division
    print(f"{a} / {b} = {div(a, b)}")

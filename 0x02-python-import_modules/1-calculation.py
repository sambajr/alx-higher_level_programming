#!/usr/bin/python3
import calculator_1 as cal

if __name__ == "__main__":
    a = 10
    b = 5

    # Print the result of addition
    print(f"{a} + {b} = {cal.add(a, b)}")

    # Print the result of subtraction
    print(f"{a} - {b} = {cal.sub(a, b)}")

    # Print the result of multiplication
    print(f"{a} * {b} = {cal.mul(a, b)}")

    # Print the result of division
    print(f"{a} / {b} = {cal.div(a, b)}")

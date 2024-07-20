"""
Author: Meng Moua
Course: CSC500
Assignment: Module 1, Part 2
"""

def main():
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")
    print('Their product:')
    print(f'\t{num1} * {num2} =', multiply(num1, num2))
    print('Their quotient:')
    print(f'\t{num1} / {num2} =', divide(num1, num2))

def multiply(num1, num2) -> str:
    """
    Multiply two numbers
    :param num1: number 1
    :param num2: number 2
    :return: a result as string
    """
    if not valid_number(num1) or not valid_number(num2):
        return "Invalid input number(s)"

    return str(int(num1) * int(num2))

def divide(numerator, denominator) -> str:
    """
    Divide two number
    :param numerator: a number for the numerator
    :param denominator: a number for the denominator
    :return: a result as string
    """
    if not valid_number(numerator) or not valid_number(denominator):
        return "Invalid input number(s)"

    result = 0
    try:
        result = int(numerator) / int(denominator)
    except Exception as e:
        return f"An error occurred: {e}"

    return str(result)

def valid_number(num) -> bool:
    """
    Validate a number
    :param num: a number
    :return: true or false
    """
    try:
        int(num)
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    main()

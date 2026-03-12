"""
Author: NickHerzb
Purpose: Implementing FizzBuzz using strandard mod operation.
Input: A number from 1 to int() limit.
Output: Starting from 1:
            if # mod 15 == 0:
                Prints "FizzBuzz"
            elif # mod 5 == 0:
                Prints "Buzz"
            elif # mod 3 == 0:
                Prints "Fizz"
            else:
                Prints #
Error Handling: If the user inputs a non-int or too large of an int then an error is printed and the program ends.
                If the user inputs a non-positive (# <= 0) int then an error is printed and the program ends.
"""


class NonPositive(Exception):
    pass


def main():

    try:
        given_input = int(input())

        if given_input <= 0:
            raise NonPositive

    except ValueError:
        print("Error: Either a non integer was given or too large of a value was given.")
        return
    except NonPositive:
        print("Error: A non positive integer was given.")
        return

    for i in range(1, given_input + 1, 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))


if __name__ == '__main__':
    main()

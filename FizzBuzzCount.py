"""
Author: NickHerzb
Purpose: Implementing FizzBuzz using counting.
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

    count_three = 0
    count_five = 0

    for i in range(1, given_input + 1, 1):
        count_three += 1
        count_five += 1
        if count_three == 3 and count_five == 5:
            print("FizzBuzz")
            count_three = 0
            count_five = 0
        elif count_three == 3:
            print("Fizz")
            count_three = 0
        elif count_five == 5:
            print("Buzz")
            count_five = 0
        else:
            print(str(i))


if __name__ == '__main__':
    main()

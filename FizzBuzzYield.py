"""
Author: NickHerzb
Purpose: Implementing FizzBuzz using yield and yield from in Python.
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


# Input: None
# Output: This is a generator that endlessly loops from 1 to 15.
#         If the index is % 15 then "FizzBuzz" is yielded.
#         Else if the index is % 5 then "Buzz" is yielded.
#         Else if the index is % 3 then "Fizz" is yielded.
#         Otherwise, the empty string is yielded.
def fizzBuzz():
    while True:
        for idx in range(1, 16):
            if idx == 3 or idx == 6 or idx == 9 or idx == 12:
                yield "Fizz"
                continue
            if idx == 5 or idx == 10:
                yield "Buzz"
                continue
            if idx == 15:
                yield "FizzBuzz"
                continue
            yield ""


def fizzBuzzWrapper(fizzBuzz):
    yield from fizzBuzz


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

    fb = fizzBuzz()
    fb_gen = fizzBuzzWrapper(fb)
    for i in range(1, given_input + 1, 1):
        fizzbuzz_res = next(fb_gen)
        print(fizzbuzz_res if fizzbuzz_res else str(i))
    fb.close()


if __name__ == '__main__':
    main()

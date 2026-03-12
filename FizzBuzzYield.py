
class NonPositive(Exception):
    pass


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

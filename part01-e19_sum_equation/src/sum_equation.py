#!/usr/bin/env python3


def sum_equation(L):
    result = "0 = 0"
    if len(L):
        result = " + ".join(map(str, L)) + f" = {sum(L)}"
    return result


def main():
    print(sum_equation([1, 5, 7]))


if __name__ == "__main__":
    main()

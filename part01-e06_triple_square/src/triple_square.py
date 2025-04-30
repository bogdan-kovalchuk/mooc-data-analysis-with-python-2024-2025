#!/usr/bin/env python3


def triple(x: int):
    return 3 * x


def square(x: int):
    return x * x


def main():
    for i in range(1, 11):
        tr = triple(i)
        sq = square(i)
        if sq > tr:
            break
        print(f"triple({i})=={tr} square({i})=={sq}")


if __name__ == "__main__":
    main()

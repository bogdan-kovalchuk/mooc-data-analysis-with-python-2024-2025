#!/usr/bin/env python3


class Prepend(object):
    def __init__(self, start: str):
        self.start = start

    def write(self, s: str):
        print(f"{self.start}{s}")


def main():
    p = Prepend("+++ ")
    p.write("Hello")


if __name__ == "__main__":
    main()

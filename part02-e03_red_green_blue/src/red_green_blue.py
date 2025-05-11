#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    pattern = r"(\d+)\s+(\d+)\s+(\d+)\s+(.+)"
    with open(filename) as f:
        lines = f.readlines()[1:]
    return ["\t".join(re.search(pattern, line).groups()) for line in lines]


def main():
    print(red_green_blue())


if __name__ == "__main__":
    main()

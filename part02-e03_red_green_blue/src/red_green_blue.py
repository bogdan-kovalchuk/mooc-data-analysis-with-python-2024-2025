#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    clead_lines = []
    with open(filename) as f:
        f.readline()
        for line in f:
            groups = re.search(r"(\d+)\s+(\d+)\s+(\d+)\s+(.+)", line).groups()
            clead_lines.append("\t".join(groups))
    return clead_lines


def main():
    print(red_green_blue())


if __name__ == "__main__":
    main()

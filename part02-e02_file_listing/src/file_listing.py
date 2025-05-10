#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename) as f:
        for l in f:
            match = re.search(r"(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+([\w.]+)", l[30:])
            t = match.groups()
            result.append((int(t[0]), t[1], int(t[2]), int(t[3]), int(t[4]), t[5]))
    return result


def main():
    print(file_listing())


if __name__ == "__main__":
    main()

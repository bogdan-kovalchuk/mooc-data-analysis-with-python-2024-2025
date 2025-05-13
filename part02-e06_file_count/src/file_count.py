#!/usr/bin/env python3

import sys


def file_count(filename):
    with open(filename) as f:
        content = f.read()
    lines = content.splitlines()
    words = content.split()
    return (len(lines), len(words), len(content))


def main():
    for filename in sys.argv[1:]:
        linecount, wordcount, charactercount = file_count(filename)
        print(f"{linecount}\t{wordcount}\t{charactercount}\t{filename}")


if __name__ == "__main__":
    main()

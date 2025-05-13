#!/usr/bin/env python3

import sys


def file_count(filename):
    linecount = 0
    wordcount = 0
    charactercount = 0
    with open(filename) as f:
        for line in f:
            linecount += 1
            wordcount += len(line.split())
            charactercount += len(line)
    return (linecount, wordcount, charactercount)


def main():
    for filename in sys.argv[1:]:
        linecount, wordcount, charactercount = file_count(filename)
        print(f"{linecount}\t{wordcount}\t{charactercount}\t{filename}")


if __name__ == "__main__":
    main()

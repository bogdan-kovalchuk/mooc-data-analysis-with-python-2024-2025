#!/usr/bin/env python3


def find_matching(L, pattern):
    return [idx for idx, word in enumerate(L) if pattern in word]


def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))


if __name__ == "__main__":
    main()

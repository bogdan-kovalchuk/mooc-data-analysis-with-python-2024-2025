#!/usr/bin/env python3


def word_frequencies(filename="src/alice.txt"):
    chars = """!"#$%&'()*,-./:;?@[]_"""
    freq = {}
    with open(filename) as f:
        for line in f:
            for word in line.split():
                cleaned = word.strip(chars)
                freq[cleaned] = freq.get(cleaned, 0) + 1
    return freq


def main():
    print(word_frequencies())


if __name__ == "__main__":
    main()

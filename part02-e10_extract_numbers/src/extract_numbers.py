#!/usr/bin/env python3


def extract_numbers(s):
    words = s.split()
    numbers = []
    for word in words:
        try:
            num = int(word)
            numbers.append(num)
        except Exception as e:
            try:
                num = float(word)
                numbers.append(num)
            except Exception as e:
                continue
    return numbers


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()

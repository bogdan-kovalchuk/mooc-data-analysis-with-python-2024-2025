#!/usr/bin/env python3


def reverse_dictionary(d):
    result = {}
    for english, finnish_lst in d.items():
        for finnish in finnish_lst:
            if finnish not in result:
                result[finnish] = [english]
            else:
                result[finnish].append(english)
    return result


def main():
    d = {
        "move": ["liikuttaa"],
        "hide": ["piilottaa", "salata"],
        "six": ["kuusi"],
        "fir": ["kuusi"],
    }

    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()

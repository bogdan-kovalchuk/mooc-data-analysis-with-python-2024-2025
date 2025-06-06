#!/usr/bin/env python3


def interleave(*lists):
    out = []
    for lst in zip(*lists):
        out.extend(lst)
    return out


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ["a", "b", "c"]))


if __name__ == "__main__":
    main()

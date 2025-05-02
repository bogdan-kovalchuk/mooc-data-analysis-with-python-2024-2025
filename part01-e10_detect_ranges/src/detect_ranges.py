#!/usr/bin/env python3


def detect_ranges(L):
    L_sorted = sorted(L)
    result = []
    i = 0
    while i < len(L_sorted):
        group_start = L_sorted[i]
        grou_end = None
        while i < len(L_sorted) - 1 and L_sorted[i] + 1 == L_sorted[i + 1]:
            grou_end = L_sorted[i + 1]
            i += 1
        if grou_end:
            result.append((group_start, grou_end + 1))
        else:
            result.append(group_start)
        i += 1
    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()

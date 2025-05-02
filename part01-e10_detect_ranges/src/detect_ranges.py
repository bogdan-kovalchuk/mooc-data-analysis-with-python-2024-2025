#!/usr/bin/env python3


def detect_ranges(nums: list):
    sorted_nums = sorted(nums)
    result = []
    idx = 0
    while idx < len(sorted_nums):
        group_start = sorted_nums[idx]
        group_end = None
        while idx < len(sorted_nums) - 1 and sorted_nums[idx] + 1 == sorted_nums[idx + 1]:
            group_end = sorted_nums[idx + 1]
            idx += 1
        if group_end:
            result.append((group_start, group_end + 1))
        else:
            result.append(group_start)
        idx += 1
    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()

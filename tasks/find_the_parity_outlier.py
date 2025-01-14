"""You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
"""


def find_outlier(integers):
    is_odd_seq = not [l % 2 for l in integers[:3]].count(True) > 1

    for i in integers:
        if is_odd_seq and i % 2 != 0:
            return i
        if not is_odd_seq and i % 2 == 0:
            return i

if __name__ == "__main__":
    assert find_outlier([17,6,8,10,6,12,24,36]) == 17
    assert find_outlier([2,6,8,10,3]) == 3
    assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160

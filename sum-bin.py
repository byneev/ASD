import math


def get_sum_of_bin():
    first = list(input())
    second = list(input())
    f_len = len(first)
    s_len = len(second)
    adder = 0
    for i in range(int(math.fabs(f_len - s_len))):
        if f_len > s_len:
            second.insert(0, "0")
        elif f_len < s_len:
            first.insert(0, "0")
    for i in range(len(first) - 1, -1, -1):
        res = adder + int(first[i]) + int(second[i])
        if res == 0:
            second[i] = "0"
            adder = 0
        if res == 1:
            adder = 0
            second[i] = "1"
        if res == 2:
            second[i] = "0"
            adder = 1
        if res == 3:
            adder = 1
            second[i] = "1"
    if adder == 1:
        second.insert(0, "1")
    return "".join(second)


print(get_sum_of_bin())

import math


def dec_to_bin():
    num = int(input())
    x = 2
    result = []
    for i in range(int(math.log2(num)), -1, -1):
        exp = x**i
        if num >= exp:
            num %= x**i
            result.append("1")
        else:
            result.append("0")
    return "".join(result)


print(dec_to_bin())

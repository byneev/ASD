from math import sqrt
import sys


def func_abc():
    a, x, b, c = sys.stdin.readline().rsplit()
    print(int(a) * (int(x) ** 2) + int(b) * int(x) + int(c))


func_abc()

import sys

stdin = sys.stdin
sys.stdin = open("input.txt", "r")


def sum():
    line = sys.stdin.readline()
    operands = line.split(" ")
    print(int(operands[0]) + int(operands[1]))
    sys.stdout.write(str(int(operands[0]) + int(operands[1])))


sum()

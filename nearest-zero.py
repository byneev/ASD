import math

# 68854238


def get_nearest_zero(n, numbers):
    start = 0
    is_first_zero = True
    for i in range(n):
        if is_first_zero:
            if numbers[i] == "0":
                for j in range(start, i):
                    numbers[j] = str(int(math.fabs(j - i)))
                start = i
                is_first_zero = False
        else:
            if numbers[i] == "0":
                for j in range(i - 1, int(start + (i - start) / 2), -1):
                    numbers[j] = str(int(math.fabs(j - i)))
                start = i
            else:
                numbers[i] = str(int(math.fabs(start - i)))
    print(" ".join(numbers))


if __name__ == "__main__":
    n = int(input())
    numbers = input().rsplit()
    get_nearest_zero(n, numbers)

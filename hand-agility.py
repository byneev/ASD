# 68853911

from collections import Counter

ROWS_COUNT = 4


def get_opportunities_count(k, arr):
    count = 0
    k *= 2
    user_input_string = "".join(arr).replace(".", "")
    counter = Counter(user_input_string)
    for key in counter.keys():
        if counter[key] <= k:
            count += 1
    print(count)


if __name__ == "__main__":
    k = int(input())
    user_input = []
    for i in range(ROWS_COUNT):
        user_input.append(input())
    get_opportunities_count(k, user_input)

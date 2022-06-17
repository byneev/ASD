def get_sum(n, arr, x):
    numbers = set()

    for num in arr:
        y = x - num
        if y in numbers:
            print(f"{num} {y}")
            break
        else:
            numbers.add(num)
    if len(numbers) == len(set(arr)):
        print("None")


get_sum(5, [1, 2, 2, 7, 12], 18)

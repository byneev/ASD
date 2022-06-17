def odd_even():
    numbers = [int(item) for item in input().rsplit()]
    result = numbers[0] % 2
    for num in numbers:
        if result != num % 2:
            return "FAIL"
    return "WIN"


print(odd_even())

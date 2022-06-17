def get_recursive_fibo():
    next, k = map(int, input().rsplit())
    k = 10**k
    if next < 2:
        print(1)
        return
    result = 2
    prev_result = 1
    temp = 0
    while next > 2:
        temp = result
        result = (result + prev_result) % k
        prev_result = temp
        next -= 1
    print(result)


get_recursive_fibo()

# import sys

# lineIn = sys.stdin.readline().split(" ")
# n = int(lineIn[0])
# m = int(lineIn[1])

# fibPrev = 0
# fib = 1
# cached = [fibPrev, fib]
# total = 0
# for curr in range(1, n):
#     fibOld = fib
#     fib = (fib + fibPrev) % m
#     fibPrev = fibOld

#     if fibPrev == 0 and fib == 1:
#         cached.pop()
#         break
#     else:
#         cached.append(fib)
# print(total)
# offset = n % len(cached)
# sys.stdout.write(str(cached[offset]))

def factorization():
    n = int(input())
    num = 2
    while n != 1:
        if num * num > n:
            print(n)
            break
        if n % num == 0:
            n = int(n / num)
            print(num, end=" ")
            num = 2
        else:
            num += 1
        if n == 2 or n == 3:
            print(n)
            break


factorization()

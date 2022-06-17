def rec_fibo(n):
    if n < 2:
        return 1
    return rec_fibo(n - 1) + rec_fibo(n - 2)


def get_recursive_fibo():
    next = int(input())
    print(rec_fibo(next))


get_recursive_fibo()

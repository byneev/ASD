def is_exp_four():
    num = int(input())

    for i in range(num):
        exp = 4**i
        if exp > num:
            return False
        elif exp == num:
            return True


print(is_exp_four())

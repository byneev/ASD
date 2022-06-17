def matrix_trans():
    n = int(input())
    m = int(input())
    arr = [[0] * n for i in range(m)]
    for i in range(n):
        current_row = input().rsplit()
        for j in range(len(current_row)):
            arr[j][i] = current_row[j]
    for row in arr:
        for item in row:
            print(item, end=" ")
        print()


matrix_trans()

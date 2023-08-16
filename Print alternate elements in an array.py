def printAl(arr, n):
    for i in range(n):
        if i % 2 == 0:
            print(arr[i], end=" ")


n = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
printAl(arr, n)

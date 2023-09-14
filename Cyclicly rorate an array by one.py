def rotate(arr, n):
    arr.insert(0, arr.pop())


n = 5
a = [1, 2, 3, 4, 5]
rotate(a, n)
print(*a)

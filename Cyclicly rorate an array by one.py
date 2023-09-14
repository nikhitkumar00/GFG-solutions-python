def rotate(arr, n):
    arr.insert(0, arr.pop())


n = int(input())
a = [int(x) for x in input().strip().split()]
rotate(a, n)
print(*a)

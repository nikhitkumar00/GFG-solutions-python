def largest(arr, n):
    arr.sort(reverse=True)
    return arr[0]


n = 5
a = [1, 8, 7, 56, 90]
print(largest(a, n))

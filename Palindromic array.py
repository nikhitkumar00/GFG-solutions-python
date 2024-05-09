def PalinArray(arr, n):
    out = True
    for i in arr:
        i = str(i)
        if i != i[::-1]:
            return False
    return out


n = 5
arr = [111, 222, 333, 444, 555]
if PalinArray(arr, n):
    print(1)
else:
    print(0)

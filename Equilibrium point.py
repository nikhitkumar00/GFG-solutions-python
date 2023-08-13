def equilibriumpoint(A, n):
    front = 0
    back = 0
    i = 0
    j = n - 1
    while i < j:
        if front <= back:
            front += A[i]
            i += 1
        else:
            back += A[j]
            j -= 1
    if front == back:
        return i + 1
    else:
        return -1


c = "20 17 42 25 32 32 30 32 37 9 2 33 31 17 14 40 9 12 36 21 8 33 6 6 10 37 12 26 21 3"
c = [int(x) for x in c.split()]
print(equilibriumpoint(c, len(c)))

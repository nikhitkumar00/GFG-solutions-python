def isSubset(a1, a2, n, m):
    freq = {}
    for i in a1:
        if i in freq:
            freq[i] +=1
        else:
            freq[i] =1

    for i in a2:
        if i in freq and freq[i] > 0:
            freq[i] -= 1
        else:
            return "No"
    return "Yes"



a1 = [11, 7, 1, 13, 21, 3, 7, 3]
a2 = [11, 3, 7, 1, 7]

print(isSubset(a1, a2, 1, 2))

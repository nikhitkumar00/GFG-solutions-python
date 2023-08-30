def kthSmallest(mat, n, k):
    list = [element for row in mat for element in row]
    list.sort()
    return list[k - 1]


n = int(input())
mat = [[0 for j in range(n)] for i in range(n)]
line1 = [int(x) for x in input().strip().split()]
k = int(input())

temp = 0
for i in range(n):
    for j in range(n):
        mat[i][j] = line1[temp]
        temp += 1

print(kthSmallest(mat, n, k))

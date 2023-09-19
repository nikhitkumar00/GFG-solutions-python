class Solution:
    def snakePattern(self, matrix):
        l = []
        for i in range(len(matrix)):
            if i % 2 == 0:
                l += matrix[i]
            else:
                l += reversed(matrix[i])
        return l


n = int(input())
values = list(map(int, input().strip().split()))
k = 0
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(values[k])
        k += 1
    matrix.append(row)
obj = Solution()
ans = obj.snakePattern(matrix)
for i in ans:
    print(i, end=" ")
print()

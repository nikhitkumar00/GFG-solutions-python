class Solution:
    def search(self, matrix, n, m, x):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == x:
                    return 1
        return 0


obj = Solution()
if obj.search([[3, 30, 38], [36, 43, 60], [40, 51, 69]], 3, 3, 493):
    print(1)
else:
    print(0)

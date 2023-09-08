# User function Template for python3


class Solution:
    def transpose(self, matrix, n):
        b = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                b[j][i] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = b[i][j]


# {
# Driver Code Starts

# Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    ob = Solution()
    ob.transpose(matrix, n)

    for row in matrix:
        print(*row)

# } Driver Code Ends

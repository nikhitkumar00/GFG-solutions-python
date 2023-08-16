# User function Template for python3


class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N - i, N + 1):
                print(i + 1, end=" ")
            print()


N = 10
ob = Solution()
ob.printTriangle(N)

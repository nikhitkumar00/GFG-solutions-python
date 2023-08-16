class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N - i):
                print(j + 1, end=" ")
            print()


N = int(input())
ob = Solution()
ob.printTriangle(N)

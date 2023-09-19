class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if j <= i and j > 0:
                    print(j, end=" ")
                else:
                    print(" ", end=" ")
            for k in range(N, 0, -1):
                if k <= i and k > 0:
                    print(k, end=" ")
                else:
                    print(" ", end=" ")
            print()


N = int(input().strip())
ob = Solution()
ob.printTriangle(N)

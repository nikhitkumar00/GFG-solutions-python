class Solution:
    def printTriangle(self, N):
        for i in range(N):
            num = 1 if i % 2 == 0 else 0
            for j in range(i + 1):
                print(num, end=" ")
                num = 1 if num == 0 else 0
            print()


N = int(input().strip())
ob = Solution()
ob.printTriangle(N)

class Solution:
    def findSum(self, A, N):
        return min(A) + max(A)


n = int(input())
a = list(map(int, input().split()))
ob = Solution()
print(ob.findSum(a, n))

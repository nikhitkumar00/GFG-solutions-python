class Solution:
    def _sum(self, arr, n):
        return sum(arr)


n = int(input())
arr = list(map(int, input().strip().split()))
ob = Solution()
ans = ob._sum(arr, n)
print(ans)

class Solution:
    def findMidSum(self, ar1, ar2, n):
        n = 2 * n
        arr = ar1 + ar2
        arr.sort()
        return arr[n // 2 - 1] + arr[n // 2]


n = 5
ar1 = [1, 2, 4, 6, 10]
ar2 = [4, 5, 6, 9, 12]
ob = Solution()
ans = ob.findMidSum(ar1, ar2, n)
print(ans)

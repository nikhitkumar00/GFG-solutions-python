class Solution:
    def maxSubArraySum(self, arr, N):
        maxx = arr[0]
        cur = 0

        for i in arr:
            if cur < 0:
                cur = 0
            cur += i
            maxx = max(maxx, cur)
        return maxx


n = int(input())
arr = [int(x) for x in input().strip().split()]
ob = Solution()
print(ob.maxSubArraySum(arr, n))

class Solution:
    def findMissing(self, arr, n):
        AP = (arr[n - 1] - arr[0]) // n
        term = arr[0]
        for i in arr:
            if i != term:
                break
            term += AP
        return term


n = 6
arr = [1, 6, 11, 16, 21, 31]
ob = Solution()
ans = ob.findMissing(arr, n)
print(ans)

class Solution:
    def maxProduct(self, arr, n):
        out = arr[0]
        curmax, curmin = 1, 1

        for i in arr:
            if i == 0:
                curmax, curmin = 1, 1
                continue
            temp = curmax
            curmax = max(curmax * i, curmin * i, i)
            curmin = min(temp * i, curmin * i, i)
            out = max(out, curmax)
        return out


n = 5
arr = [6, -3, -10, 0, 2]
ob = Solution()
ans = ob.maxProduct(arr, n)
print(ans)

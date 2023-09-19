class Solution:
    def findTwoElement(self, arr, n):
        sett = set(arr)
        return sum(arr) - sum(sett), ((n * (n + 1)) // 2) - sum(sett)


n = 3
arr = [1, 3, 3]
ob = Solution()
ans = ob.findTwoElement(arr, n)
print(str(ans[0]) + " " + str(ans[1]))

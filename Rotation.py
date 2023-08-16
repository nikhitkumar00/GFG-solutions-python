class Solution:
    def findKRotation(self, arr, n):
        return arr.index(min(arr))


n = 5
a = [2, 3, 4, 5, 1]
ob = Solution()
ans = ob.findKRotation(a, n)
print(ans)

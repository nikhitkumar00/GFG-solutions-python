class Solution:
    def countZeroes(self, arr, n):
        arr.reverse()
        count = 0
        for i in arr:
            if i == 0:
                count += 1
            else:
                break
        return count


n = 9999
arr = [1, 1, 1, 1, 0, 0, 0, 0]
ob = Solution()
ans = ob.countZeroes(arr, n)
print(ans)

class Solution:
    def isPowerofTwo(self, n):
        if n <= 0:
            return False
        else:
            return n & (n - 1) == 0


n = int(input())
ob = Solution()
if ob.isPowerofTwo(n):
    print("YES")
else:
    print("NO")

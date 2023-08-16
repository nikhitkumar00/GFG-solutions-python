class Solution:
    def nPr(self, n, r):
        out = 1
        for i in range(r):
            out = out * n
            n = n - 1
        return out


n, r = [int(x) for x in input().split()]
ob = Solution()
print(ob.nPr(n, r))

class Solution:
    def minValue(self, a, b, n):
        a.sort()
        b.sort(reverse=True)
        out = 0
        for i in range(n):
            out = out + (a[i] * b[i])
        return out


n = int(input())
a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]
ob = Solution()
print(ob.minValue(a, b, n))

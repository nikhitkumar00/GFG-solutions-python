class Solution:
    def doUnion(self, a, n, b, m):
        a = set(a)
        b = set(b)
        return len(a.union(b))


n, m = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]
ob = Solution()
print(ob.doUnion(a, n, b, m))

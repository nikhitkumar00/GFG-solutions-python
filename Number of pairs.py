class Solution:
    def countPairs(self, a, b):
        out = 0
        for i in a:
            for j in b:
                if i**j > j**i:
                    out += 1
        return out


a, b = [2, 1, 6], [1, 5]
ob = Solution()
print(ob.countPairs(a, b))

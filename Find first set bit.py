class Solution:
    def getFirstSetBit(self, n):
        binary = bin(n)[2:][::-1]
        out = 0
        for i in binary:
            out += 1
            if i == "1":
                return out
        return 0


n = 0
ob = Solution()
print(ob.getFirstSetBit(n))

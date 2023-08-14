class Solution:
    def getFirstSetBit(self, n):
        n = bin(n)[:1:-1]
        out = 0
        for i in n:
            if i == "1":
                break
            out += 1
        return out + 1 if n != "0" else 0


n = 0
ob = Solution()
print(ob.getFirstSetBit(n))

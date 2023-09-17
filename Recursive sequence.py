class Solution:
    def sequence(self, N):
        out = 0
        num = 1

        for i in range(N):
            cur = 1
            for j in range(i + 1):
                cur *= num
                num += 1
            out += cur
        return out


N = 5
ob = Solution()
print(ob.sequence(N))

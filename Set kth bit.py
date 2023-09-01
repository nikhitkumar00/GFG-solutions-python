class Solution:
    def setKthBit(self, N, K):
        mask = 1 << K
        return N | mask


N = 10
K = 2
ob = Solution()
ans = ob.setKthBit(N, K)
print(ans)

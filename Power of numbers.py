class Solution:
    def power(self, N, R):
        if R == 1:
            return N
        halfpower = self.power(N, R // 2)
        if R % 2 == 0:
            return (halfpower * halfpower) % 1000000007
        else:
            return (N * halfpower * halfpower) % 1000000007


N = "21"
R = N[::-1]
ob = Solution()
ans = ob.power(int(N), int(R))
print(ans)

class Solution:
    def rotate(self, N, D):
        D = D % 16
        binary = bin(N)[2:]
        binary = "0" * (16 - len(binary)) + binary
        left = int(binary[D:] + binary[:D], 2)
        right = int(binary[-D:] + binary[:-D], 2)
        return [left, right]


n, d = 18, 20
ob = Solution()
ans = ob.rotate(n, d)
print(ans[0])
print(ans[1])

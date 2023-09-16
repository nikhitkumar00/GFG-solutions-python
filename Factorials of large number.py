class Solution:
    def factorial(self, N):
        out = 1
        for i in range(2, N + 1):
            out *= i
        return list(str(out))


N = int(input())
ob = Solution()
ans = ob.factorial(N)
for i in ans:
    print(i, end="")
print()

class Solution:
    def missingNumber(self, array, n):
        total = n * (n + 1) // 2
        return total - sum(array)


n = int(input())
a = list(map(int, input().split()))
s = Solution().missingNumber(a, n)
print(s)

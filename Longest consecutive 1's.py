class Solution:
    def maxConsecutiveOnes(self, N):
        binary = bin(N)[2:]
        return max(map(len, binary.split("0")))


n = int(input())
obj = Solution()
print(obj.maxConsecutiveOnes(n))

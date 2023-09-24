class Solution:
    def count(self, coins, N, Sum):
        dp = [0] * (Sum + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, Sum + 1):
                dp[i] += dp[i - c]

        return dp[Sum] if dp[Sum] != 0 else 0


sum, N = list(map(int, input().strip().split()))
coins = list(map(int, input().strip().split()))
ob = Solution()
print(ob.count(coins, N, sum))

class Solution:
    def knapSack(self, W, wt, val, n):
        cache = [[-1 for i in range(W + 1)] for i in range(n + 1)]

        def knapsack(W, wt, val, n):
            if W == 0 or n == 0:
                return 0

            if cache[n][W] != -1:
                return cache[n][W]

            if wt[n - 1] > W:
                out = knapsack(W, wt, val, n - 1)
            else:
                out = max(
                    val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1),
                    knapsack(W, wt, val, n - 1),
                )

            cache[n][W] = out
            return out

        return knapsack(W, wt, val, n)


n = int(input())
W = int(input())
val = list(map(int, input().strip().split()))
wt = list(map(int, input().strip().split()))
ob = Solution()
print(ob.knapSack(W, wt, val, n))

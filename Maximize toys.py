class Solution:
    def toyCount(self, N, K, arr):
        arr.sort()
        amount = K
        count = 0
        for i in arr:
            if i > amount:
                break
            count += 1
            amount -= i
        return count


N, K = [int(x) for x in input().split()]
arr = input().split()
for it in range(N):
    arr[it] = int(arr[it])
ob = Solution()
print(ob.toyCount(N, K, arr))

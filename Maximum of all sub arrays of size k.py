class Solution:
    def max_of_subarrays(self, arr, n, k):
        a = []
        big = max(arr[0:k])
        a.append(big)
        for i in range(1, n - k + 1):
            if arr[i - 1] == big:
                big = max(arr[i : i + k])
            else:
                big = max(big, arr[i + k - 1])
            a.append(big)
        return a


n, k = 9, 3
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
ob = Solution()
res = ob.max_of_subarrays(arr, n, k)
for i in range(len(res)):
    print(res[i], end=" ")
print()

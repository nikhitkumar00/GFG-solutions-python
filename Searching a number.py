class Solution:
    def search(self, arr, n, k):
        return arr.index(k) + 1 if k in arr else -1


n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
ob = Solution()
ans = ob.search(arr, n, k)
print(ans)

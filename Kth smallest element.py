class Solution:
    def kthSmallest(self, arr, l, r, k):
        arr.sort()
        return arr[k - 1]


n = int(input())
arr = list(map(int, input().strip().split()))
k = int(input())
ob = Solution()
print(ob.kthSmallest(arr, 0, n - 1, k))

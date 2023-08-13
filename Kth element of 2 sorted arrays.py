class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        arr = arr1 + arr2
        arr.sort()
        return arr[k - 1]


k = int(input())
a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]
ob = Solution()
print(ob.kthElement(a, b, k))

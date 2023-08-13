class Solution:
    def searchInsertK(self, Arr, N, k):
        def binary(a, low, high, key):
            mid = (low + high) // 2
            if a[mid - 1] < key and a[mid + 1] > key:
                return mid
            elif key < a[mid]:
                return binary(a, low, mid, key)
            else:
                return binary(a, mid + 1, high, key)

        return binary(Arr, 0, N, k)


N = int(input())
Arr = input().split()
for itr in range(N):
    Arr[itr] = int(Arr[itr])
k = int(input())
ob = Solution()
print(ob.searchInsertK(Arr, N, k))

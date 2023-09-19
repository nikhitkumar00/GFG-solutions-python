class Solution:
    def binarysearch(self, arr, n, k):
        def binary(l, h):
            if l > h:
                return -1
            else:
                mid = (l + h) // 2
                if arr[mid] == k:
                    return mid
                elif arr[mid] < k:
                    return binary(mid + 1, h)
                else:
                    return binary(l, mid - 1)

        return binary(0, n - 1)


n = 5
arr = [1, 2, 3, 4, 5]
k = 3.5
ob = Solution()
print(ob.binarysearch(arr, n, k))

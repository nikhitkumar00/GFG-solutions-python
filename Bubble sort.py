class Solution:
    def bubbleSort(self, arr, n):
        for i in range(n - 1):
            for j in range(n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


n = 10
arr = [9,8,7,6,5,4,3,2,1,0]
ob = Solution()
ob.bubbleSort(arr, n)
for i in arr:
    print(i, end=" ")
print()

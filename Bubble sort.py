class Solution:
    def bubbleSort(self, arr, n):
        for i in range(n - 1):
            for j in range(n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


n = int(input())
arr = list(map(int, input().strip().split()))
ob = Solution()
ob.bubbleSort(arr, n)
for i in arr:
    print(i, end=" ")
print()

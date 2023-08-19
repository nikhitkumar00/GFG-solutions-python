class Solution:
    def rearrange(self, arr, n):
        high = n - 1
        low = 0
        array = []
        i = 0
        while high >= low:
            if i % 2 == 0:
                array.append(arr[high])
                high -= 1
            else:
                array.append(arr[low])
                low += 1
            i += 1
        for i in range(n):
            arr[i] = array[i]


# Output:110 10 100 20 90 30 80 40 70 50 60
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
ob = Solution()
ob.rearrange(arr, len(arr))
for i in arr:
    print(i, end=" ")

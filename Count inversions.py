class Solution:
    def inversionCount(self, arr, n):
        count = 0
        for j in range(1, n):
            for i in range(1, n):
                if arr[i - 1] > arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    count += 1
        return count


n = 5
a = [2, 4, 1, 3, 5]
obj = Solution()
print(obj.inversionCount(a, n))

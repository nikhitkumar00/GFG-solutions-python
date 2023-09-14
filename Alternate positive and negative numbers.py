class Solution:
    def rearrange(self, arr, n):
        negative = [i for i in arr if i < 0]
        positive = [i for i in arr if i >= 0]
        
        for i in range(n):
            if i % 2 == 0:
                arr[i] = positive.pop(0) if positive else negative.pop(0)
            else:
                arr[i] = negative.pop(0) if negative else positive.pop(0)


n = 10
arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
ob = Solution()
ob.rearrange(arr, n)
for x in arr:
    print(x, end=" ")
print()

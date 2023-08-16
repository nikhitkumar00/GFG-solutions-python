class Solution:
    def nextLargerElement(self, arr, n):
        dic = dict.fromkeys(arr,-1)
        for i in arr:
            


n = 5
a = [6, 8, 0, 1, 3]
obj = Solution()
res = obj.nextLargerElement(a, n)
for i in range(len(res)):
    print(res[i], end=" ")
print()

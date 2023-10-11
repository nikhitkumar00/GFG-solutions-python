class Solution:
    def subArrayExists(self, arr, n):
        dic = {}
        current = 0
        for index, i in enumerate(arr):
            current += i
            if current in dic or current == 0:
                return True
            dic[current] = index
        return False


n = int(input())
arr = [int(x) for x in input().strip().split()]
if Solution().subArrayExists(arr, n):
    print("Yes")
else:
    print("No")

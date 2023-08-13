class Solution:
    def printLargest(self, arr):
        arr.sort(key=lambda x: x * 10, reverse=True)
        result = "".join(arr)
        return result if result[0] != "0" else "0"


import functools

n = int(input())
arr = list(map(str, input().strip().split()))
ob = Solution()
ans = ob.printLargest(arr)
print(ans)

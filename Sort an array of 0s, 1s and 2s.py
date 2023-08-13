# User function Template for python3


class Solution:
    def sort012(self, arr, n):
        return arr.sort()


n = int(input())
arr = [int(x) for x in input().strip().split()]
ob = Solution()
ob.sort012(arr, n)
for i in arr:
    print(i, end=" ")
print()

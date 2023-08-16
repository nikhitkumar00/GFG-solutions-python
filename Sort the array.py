# User function Template for python3
class Solution:
    def sortArr(self, arr, n):
        return sorted(arr)


n = int(input())
arr = list(map(int, input().strip().split()))
obj = Solution()
ans = obj.sortArr(arr, n)
for i in ans:
    print(i, end=" ")

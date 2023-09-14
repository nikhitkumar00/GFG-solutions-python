class Solution:
    def Sorted(self, s):
        s.sort()


n = int(input())
arr = list(map(int, input().strip().split()))
ob = Solution()
ob.Sorted(arr)
for e in range(len(arr)):
    print(arr.pop(), end=" ")
print()

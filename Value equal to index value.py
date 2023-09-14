class Solution:
    def valueEqualToIndex(self, arr, n):
        out = []
        for index, i in enumerate(arr):
            if index + 1 == i:
                out.append(i)
        return out


n = int(input())
arr = list(map(int, input().strip().split()))
ob = Solution()
ans = ob.valueEqualToIndex(arr, n)
if len(ans) == 0:
    print("Not Found")
else:
    for x in ans:
        print(x, end=" ")
    print()

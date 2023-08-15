class Solution:
    def print2largest(self, arr, n):
        arr.sort(reverse=True)
        for i in arr:
            if i != arr[0]:
                return i
        return -1


n = int(input())
arr = list(map(int, input().strip().split()))
ob = Solution()
ans = ob.print2largest(arr, n)
print(ans)

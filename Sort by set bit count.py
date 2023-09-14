class Solution:
    def sortBySetBitCount(self, arr, n):
        arr.sort(key=lambda x: bin(x).count("1"), reverse=True)
        return arr


n = int(input())
arr = [int(x) for x in input().strip().split()]
ob = Solution()
ob.sortBySetBitCount(arr, n)
print(*arr)

class Solution:
    def search(self, A: list, l: int, h: int, key: int):
        return A.index(key) if key in A else -1


n = int(input())
A = [int(x) for x in input().split()]
k = int(input())
ob = Solution()
print(ob.search(A, 0, n - 1, k))

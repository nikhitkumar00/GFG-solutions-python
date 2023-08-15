class Solution:
    def search(self, arr, N, X):
        return arr.index(X) if X in arr else -1


N = 5
A = [1, 2, 3, 4, 5]
x = 5
ob = Solution()
print(ob.search(A, N, x))

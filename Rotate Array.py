class Solution:
    def rotateArr(self, A, D, N):
        A.reverse()
        D = D % N
        A[: N - D] = reversed(A[: N - D])
        A[N - D :] = reversed(A[N - D :])
        return A

N = 5
D = 11
A = [1, 2, 3, 4, 5]
ob = Solution()
ob.rotateArr(A, D, N)
for i in A:
    print(i, end=" ")

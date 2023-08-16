class Solution:
    def remove_duplicate(self, A, N):
        dic = {}
        count = 0
        index = 0
        while index < N:
            if A[index] in dic:
                A.pop(index)
                N -=1
            else:
                dic[A[index]] = 1
                count += 1
                index += 1
        return count



N = 12
A = list(map(int, "2 2 2 2 2 2 22 2 2 2 22 3".strip().split()))
ob = Solution()
n = ob.remove_duplicate(A, N)
for i in range(n):
    print(A[i], end=" ")
print()

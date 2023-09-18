class Solution:
    def countDistinct(self, A, N, K):
        dic = {}
        out = []
        for i in range(N):
            dic[A[i]] = dic[A[i]] + 1 if A[i] in dic else 1
            if i + 1 >= K:
                out.append(len(dic))
                dic[A[i - K + 1]] -= 1
                if dic[A[i - K + 1]] == 0:
                    del dic[A[i - K + 1]]
        return out


n, k = 7, 4
arr = [1, 2, 1, 3, 4, 2, 3]
res = Solution().countDistinct(arr, n, k)
for i in res:
    print(i, end=" ")
print()

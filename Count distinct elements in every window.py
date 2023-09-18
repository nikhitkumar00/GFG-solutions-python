class Solution:
    def countDistinct(self, A, N, K):
        dic = {}
        out = []
        for i in range(N):
            if A[i] in dic:
                dic[A[i]] += 1
            else:
                dic[A[i]] = 1
            if i + 1 >= K:
                out.append(len(dic))
                dic[A[i - K + 1]] -= 1
                if dic[A[i - K + 1]] == 0:
                    del dic[A[i - K + 1]]
        return out


n, k = 3, 2
arr = [4, 1, 1]
res = Solution().countDistinct(arr, n, k)
for i in res:
    print(i, end=" ")
print()

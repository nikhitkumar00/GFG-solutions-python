class Solution:
    def allPairs(self, A, B, N, M, X):
        c = []
        dica = dict.fromkeys(A, 0)
        dicb = dict.fromkeys(B, 0)
        for i in dica:
            if (X - i) in dicb:
                c.append([i, X - i])
        c.sort(key=lambda x: x[0])
        return c


sz = [int(x) for x in input().strip().split()]
N, M, X = sz[0], sz[1], sz[2]
A = [int(x) for x in input().strip().split()]
B = [int(x) for x in input().strip().split()]
ob = Solution()
answer = ob.allPairs(A, B, N, M, X)
sz = len(answer)

if sz == 0:
    print(-1)

else:
    for i in range(sz):
        if i == sz - 1:
            print(*answer[i])
        else:
            print(*answer[i], end=", ")

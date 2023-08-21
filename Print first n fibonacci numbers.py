class Solution:
    def printFibb(self, n):
        dic = {1: 1, 2: 1}
        out = [1, 1]
        for i in range(3, n + 1):
            dic[i] = dic[i - 1] + dic[i - 2]
            out.append(dic[i])
        return out[:n]


res = Solution().printFibb(5)
for i in range(len(res)):
    print(res[i], end=" ")
print()

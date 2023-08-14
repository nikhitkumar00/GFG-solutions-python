class Solution:
    def findSingle(self, N, arr):
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        out = []
        for i in dic:
            if dic[i] == 1:
                out.append(i)
        return out


N = 4
arr = [1, 2, 3, 4, 5, 6, 1, 2, 3, 5, 6]
for itr in range(N):
    arr[itr] = int(arr[itr])

ob = Solution()
print(ob.findSingle(N, arr))

class Solution:
    def duplicates(self, arr, n):
        dic = {}
        l = []
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] > 1:
                l.append(i)
        return sorted(l) if len(l) > 0 else [-1]


n = 2
arr = [0,0]
res = Solution().duplicates(arr, n)
for i in res:
    print(i, end=" ")
print()

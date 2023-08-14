class Solution:
    def singleNumber(self, nums):
        dic = {}
        l = []
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] == 1:
                l.append(i)
        return sorted(l)


n = int(input())
v = list(map(int, "16 17 13 7 23 24 13 26 23 24 16 7 19 3 26 17".split()))
ob = Solution()
ans = ob.singleNumber(v)
for i in ans:
    print(i, end=" ")
print()

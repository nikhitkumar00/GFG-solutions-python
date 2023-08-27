class Solution:
    def minIndexChar(self, Str, pat):
        dic = {}
        for index, i in enumerate(Str):
            if i not in dic:
                dic[i] = index
        small = 9999
        for i in pat:
            if i in dic and dic[i] < small:
                small = dic[i]
        return small if small != 9999 else -1


s = "adcffaet"
p = "onkl"
obj = Solution()
ans = obj.minIndexChar(s, p)
print(ans)

class Solution:
    def firstRepChar(self, s):
        dic = set()
        for i in s:
            if i in dic:
                return i
            else:
                dic.add(i)
        return -1

s = "abcasbd"
solObj = Solution()
print(solObj.firstRepChar(s))
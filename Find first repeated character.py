class Solution:
    def firstRepChar(self, s):
        dic = {}
        for i in s:
            if i in dic:
                return i
            else:
                dic[i] = 1
        return -1

s = "abc"
solObj = Solution()
print(solObj.firstRepChar(s))
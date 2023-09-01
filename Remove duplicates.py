class Solution:
    def removeDups(self, S):
        dic = {}
        out = ""
        for i in S:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 0
                out += i
        return out


s = "gfg"
ob = Solution()
answer = ob.removeDups(s)
print(answer)

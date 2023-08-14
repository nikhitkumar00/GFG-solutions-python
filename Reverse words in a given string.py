# User function Template for python3

class Solution:
    def reverseWords(self,S):
        l = S.split('.')
        out = l[len(l)-1]
        for i in range(len(l)-2,-1,-1):
            out = out + '.' + l[i]
        return out
        
s = "i.like.this.program.very.much"
obj = Solution()
print(obj.reverseWords(s))
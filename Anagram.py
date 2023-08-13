class Solution:
    def isAnagram(self,a,b):
        if len(a) != len(b):
            return False
        dicta = dict.fromkeys(a,0)
        dictb = dict.fromkeys(b,0)
        for i in a:
            dicta[i] += 1
        for i in b:
            dictb[i] += 1
        if dicta != dictb:
            return False
        return True
        
a,b=map(str,input().strip().split())
if(Solution().isAnagram(a,b)):
    print("YES")
else:
    print("NO") 
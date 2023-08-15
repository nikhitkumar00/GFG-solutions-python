class Solution:
    def ispar(self,x):
        l =[]
        for i in x:
            if i in "({[":
                l.append(i)
            elif l and i in "]})":
                j = l[-1]
                if i =="]" and j == "[":
                    l.pop()
                elif i =="}" and j == "{":
                    l.pop()
                elif i ==")" and j == "(":
                    l.pop()
                else:
                    return False
            else:
                return False
        return False if l else True
s = "{([])}"
obj = Solution()
if obj.ispar(s):
    print("balanced")
else:
    print("not balanced")
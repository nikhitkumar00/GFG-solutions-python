class Solution:
    def transform(self, s):
        l = s.split(" ")
        for i in range(len(l)):
            l[i] = l[i][0].upper() + l[i][1:]
        return " ".join(l)


s = "my name is nikhit"
ob = Solution()
print(ob.transform(s))

class Solution:
    def areIsomorphic(self, str1, str2):
        if len(str1) != len(str2):
            return False
        dic1 = {}
        dic2 = {}
        dic = {}
        for i in range(len(str1)):
            dic1[str1[i]] = dic1[str1[i]] + 1 if str1[i] in dic1 else 1
            dic2[str2[i]] = dic2[str2[i]] + 1 if str2[i] in dic2 else 1
            if str1[i] in dic:
                if dic[str1[i]] != str2[i]:
                    return False
            else:
                dic[str1[i]] = str2[i]
        for i in range(len(str1)):
            if dic1[str1[i]] != dic2[str2[i]]:
                return False
        return True


s = "ehj"
p = "el"
ob = Solution()
if ob.areIsomorphic(s, p):
    print(1)
else:
    print(0)

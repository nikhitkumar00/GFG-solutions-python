class Solution:
    def isRotated(self, str1, str2):
        new1 = str1[2:] + str1[:2]
        new2 = str1[-2:] + str1[:-2]
        return 1 if str2 == new1 or str2 == new2 else 0


s = "fsbcnuvqhffbsaqxwp"
p = "wpfsbcnuvqhffbsaqx"
if Solution().isRotated(s, p):
    print(1)
else:
    print(0)

class Solution:
    def wifiRange(self, n, s, x):
        l = list(s)
        for index,i in enumerate(l):
            if i == "1":
                for j in range(index-x,index+x+1):
                    if j >=0 and j<n and l[j] != "1":
                        l[j] = 1
        return 0 if "0" in l else 1
            


N, X = 6, 1
S = "110100"
ob = Solution()
ans = ob.wifiRange(N, S, X)
if ans:
    print(1)
else:
    print(0)

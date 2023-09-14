# User function Template for python3


class Solution:
    def rremove(self, S):
        i = 0
        S += "1"
        out = ""
        flag = 0
        flagg = 0
        while i < len(S) - 1:
            if S[i] != S[i + 1] and flag == 0:
                out += S[i]
            elif S[i] != S[i + 1]:
                flag = 0
            else:
                flag = 1
                flagg = 1
            i += 1
        return out if flagg == 0 else self.rremove(out)


S = "banna"
ob = Solution()
print(ob.rremove(S))

class Solution:
    def UncommonChars(self, A, B):
        out = []
        dica = dict.fromkeys(A, 0)
        dicb = dict.fromkeys(B, 0)
        for i in dica:
            if i not in dicb:
                out.append(i)
        for i in dicb:
            if i not in dica:
                out.append(i)
        out.sort()
        ret = "".join(out)
        return ret if len(ret) != 0 else -1


A = "g"
B = "g"
ob = Solution()
print(ob.UncommonChars(A, B))

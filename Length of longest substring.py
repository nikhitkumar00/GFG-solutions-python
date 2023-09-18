class Solution:
    def longestUniqueSubsttr(self, S):
        sett = set()
        l = 0
        out = 0

        for r in range(len(S)):
            while S[r] in sett:
                sett.remove(S[l])
                l += 1
            sett.add(S[r])
            out = max(out, r - l + 1)

        return out


s = input().strip()
ob = Solution()
print(ob.longestUniqueSubsttr(s))

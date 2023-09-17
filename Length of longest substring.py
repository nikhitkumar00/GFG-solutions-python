class Solution:
    def longestUniqueSubsttr(self, S):
        s = set()
        l = 0
        out = 0

        for r in range(len(S)):
            while S[r] in s:
                s.remove(S[l])
                l += 1
            s.add(S[r])
            out = max(out, r - l + 1)

        return out


s = input().strip()
ob = Solution()
print(ob.longestUniqueSubsttr(s))

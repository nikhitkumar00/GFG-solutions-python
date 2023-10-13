class Solution:
    def longestSubstrDistinctChars(self, S):
        left = 0
        right = 0
        dic = {}
        maxx = -1
        while right < len(S):
            if S[right] in dic:
                dic.pop(S[left], None)
                left += 1
            else:
                dic[S[right]] = 1
                right += 1
            maxx = max(len(dic), maxx)
        return maxx


S = "aaa"
solObj = Solution()
ans = solObj.longestSubstrDistinctChars(S)
print(ans)

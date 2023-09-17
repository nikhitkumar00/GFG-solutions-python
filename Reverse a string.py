class Solution:
    def reverseWord(self, str: str) -> str:
        return str[::-1]


s = input()
ob = Solution()
print(ob.reverseWord(s))

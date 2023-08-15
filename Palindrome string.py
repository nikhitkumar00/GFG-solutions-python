class Solution:
	def isPalindrome(self, S):
		l = len(S)
		for i in range(l//2):
			if S[i] != S[l-i-1]:
				return 0
		return 1
S = "abacaba"
ob = Solution()
answer = ob.isPalindrome(S)
print(answer)
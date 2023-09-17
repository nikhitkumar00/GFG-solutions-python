class Solution:
    def maxLength(self, S):
        stack = [-1]
        maxx = 0
        for i, num in enumerate(S):
            if num == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxx = max(maxx, i - stack[-1])
                else:
                    stack.append(i)
        return maxx


S = input()
ob = Solution()
print(ob.maxLength(S))

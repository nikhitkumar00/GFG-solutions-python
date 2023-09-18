class Solution:
    def maxLength(self, S):
        stack = [-1]
        maxx = 0
        for index, num in enumerate(S):
            if num == "(":
                stack.append(index)
            else:
                stack.pop()
                if stack:
                    maxx = max(maxx, index - stack[-1])
                else:
                    stack.append(index)
        return maxx


S = ")()()))("
ob = Solution()
print(ob.maxLength(S))

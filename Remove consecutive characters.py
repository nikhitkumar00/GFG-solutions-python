class Solution:
    def removeConsecutiveCharacter(self, S):
        stack = []
        for i in S:
            if stack and stack[-1] == i:
                continue
            stack.append(i)

        out = ""
        for i in stack:
            out += i
        return out


s = input()
ob = Solution()
print(ob.removeConsecutiveCharacter(s))

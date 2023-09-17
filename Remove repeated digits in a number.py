class Solution:
    def modify(self, N):
        stack = []
        out = ""
        for i in str(N):
            if stack and stack[-1] == i:
                continue
            stack.append(i)
        for i in stack:
            out += i
        return out


num = int(input())
solObj = Solution()
print(solObj.modify(num))

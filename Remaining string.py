class Solution:
    def printString(self, S, ch, count):
        temp = 0
        if count == 0:
            return S
        for i in range(len(S)):
            if S[i] == ch:
                temp += 1
                if temp == count:
                    return S[i + 1 :] if len(S[i + 1 :]) > 0 else "Empty string"
        return "Empty string"


s = "ieiei"
ch = "i"
count = 3
ob = Solution()
answer = ob.printString(s, ch, count)
print(answer)

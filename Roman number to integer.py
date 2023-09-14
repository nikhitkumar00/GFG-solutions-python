class Solution:
    def romanToDecimal(self, S):
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        out = 0
        prev = 0
        for i in reversed(S):
            if dic[i] >= prev:
                out += dic[i]
            else:
                out -= dic[i]
            prev = dic[i]
        return out


ob = Solution()
S = "II"
print(ob.romanToDecimal(S))

class Solution:
    def FirstNonRepeating(self, A):
        dic = {}
        non_repeating = []
        out = ""

        for i in A:
            if i in dic:
                dic[i] += 1
                if i in non_repeating:
                    non_repeating.remove(i)
            else:
                dic[i] = 1
                non_repeating.append(i)

            if non_repeating:
                out += non_repeating[0]
            else:
                out += "#"
        return out


A = "aabc"
ob = Solution()
ans = ob.FirstNonRepeating(A)
print(ans)

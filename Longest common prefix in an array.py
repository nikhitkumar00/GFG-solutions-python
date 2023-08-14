class Solution:
    def longestCommonPrefix(self, arr, n):
        def findcommon(a, b):
            out = ""
            for i in range(min(len(a), len(b))):
                if a[i] == b[i]:
                    out += a[i]
                else:
                    return out
            return out

        common = arr[0]
        for i in range(n - 1):
            common = findcommon(common, arr[i + 1])
        return common if len(common) > 0 else -1


n = 4
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
ob = Solution()
print(ob.longestCommonPrefix(arr, n))

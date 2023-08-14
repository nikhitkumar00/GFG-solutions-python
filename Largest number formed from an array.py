class Solution:
    def printLargest(self, arr):
        arr.sort(key = lambda x : x * 10, reverse=True)
        result = "".join(arr)
        return result if result[0] != "0" else "0"


"""
5555555555
3333333333
30303030303030303030
34343434343434343434
9999999999
"""

n = 5
arr = list(map(str, "5 3 30 34 5 9".strip().split()))
ob = Solution()
ans = ob.printLargest(arr)
print(ans)

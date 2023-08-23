class Solution:
    def findOnce(self, arr: list, n: int):
        try:
            for i in range(0, n, 2):
                assert arr[i+1]
                if arr[i] != arr[i + 1]:
                    return arr[i]
        except:
            return arr[n-1]


arr = [1, 1, 2, 2, 3, 3, 4, 4, 50, 50, 65]
ob = Solution()
print(ob.findOnce(arr, len(arr)))

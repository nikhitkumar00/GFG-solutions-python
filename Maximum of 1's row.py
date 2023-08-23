class Solution:
    def maxOnes(self, Mat, N, M):
        maxi, ini = -999, -1
        for index, i in enumerate(Mat):
            if i.count(1) > maxi:
                maxi, ini = i.count(1), index
        return ini


ob = Solution()
print(ob.maxOnes([[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 1]], 4, 4))

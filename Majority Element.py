class Solution:
    def majorityElement(self, A, N):
        dic = dict.fromkeys(A, 0)
        for i in A:
            dic[i] += 1
        return max(dic) if dic[max(dic)] > N // 2 else -1


import math

N = 6
A = [3, 1, 3, 3, 2, 3]
obj = Solution()
print(obj.majorityElement(A, N))

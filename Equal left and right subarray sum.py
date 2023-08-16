class Solution:
    def equalSum(self, A, N):
        l = 0
        r = sum(A)
        for index,i in enumerate(A):
            r -= i
            if l == r:
                return index+1
            l += i
        return -1


N = 42
s = "4 42 27 16 28 3 4 5 9 3 31 5 5 29 10 18 35 35 33 19 41 23 8 32 9 5 8 18 35 13 6 7 6 10 11 13 37 2 25 7 28 43"
A = list(map(int,s.split()))
ob = Solution()
print(ob.equalSum(A, N))

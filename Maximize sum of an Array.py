class Solution:
    def Maximize(self, a, n):
        out = 0
        a.sort()
        for index, i in enumerate(a):
            out += index * i
        return out % 1000000007


for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.Maximize(arr, n))

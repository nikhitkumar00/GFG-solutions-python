class Solution:
    def reverse(self, St):
        St.reverse()


N = int(input())
St = list(map(int, input().split()))
ob = Solution()
ob.reverse(St)
print(*St)

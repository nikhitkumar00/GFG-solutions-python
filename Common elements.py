class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        dic1 = dict.fromkeys(A, 0)
        dic2 = dict.fromkeys(B, 0)
        dic3 = dict.fromkeys(C, 0)
        i = [a for a in dic1 if a in dic2 and a in dic3]
        return sorted(i)


n1, n2, n3 = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ob = Solution()
res = ob.commonElements(A, B, C, n1, n2, n3)
if len(res) == 0:
    print(-1)
else:
    for i in range(len(res)):
        print(res[i], end=" ")
    print()

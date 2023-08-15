class Solution:
    def relativeSort(self, A1, N, A2, M):
        dic = {x: index for index, x in enumerate(A2)}

        def priority(n):
            if n in dic:
                return dic[n]
            else:
                return n + 9999

        A1.sort(key=priority)
        return A1


#       2 2 1 1 8 8 3 5 6 7 9

n, m = 11, 4
a1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
a2 = [2, 1, 8, 3]

ob = Solution()
a1 = ob.relativeSort(a1, n, a2, m)
print(*a1, end=" ")

print()

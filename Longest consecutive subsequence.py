class Solution:
    def findLongestConseqSubseq(self, arr, N):
        arr.sort()
        count = 1
        out = 1
        for i in range(1, N):
            if arr[i] != arr[i - 1]:
                if arr[i] - 1 == arr[i - 1]:
                    count += 1
                    if out < count:
                        out = count
                else:
                    count = 1
        return out


n = 5
a = [2, 0, 1, 1, 4]
print(Solution().findLongestConseqSubseq(a, n))

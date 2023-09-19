class Solution:
    def peakElement(self, arr, n):
        arr.insert(0, 0)
        arr.insert(n + 1, 0)
        for i in range(1, len(arr) - 1):
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return i - 1
        return -1


n = 3
arr = [1, 2, 3]
index = Solution().peakElement(arr.copy(), n)
flag = False
if index < 0 or index >= n:
    flag = False
else:
    if index == 0 and n == 1:
        flag = True
    elif index == 0 and arr[index] >= arr[index + 1]:
        flag = True
    elif index == n - 1 and arr[index] >= arr[index - 1]:
        flag = True
    elif arr[index - 1] <= arr[index] and arr[index] >= arr[index + 1]:
        flag = True
    else:
        flag = False

if flag:
    print(1)
else:
    print(0)

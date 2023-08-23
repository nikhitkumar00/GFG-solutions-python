class Solution:
    def merge(self, arr, l, m, r):
        low = l
        mid = m + 1
        high = r
        b = []
        while low <= m and mid <= high:
            if arr[low] <= arr[mid]:
                b.append(arr[low])
                low += 1
            else:
                b.append(arr[mid])
                mid += 1
        while low <= m:
            b.append(arr[low])
            low += 1
        while mid <= high:
            b.append(arr[mid])
            mid += 1
        for i in range(len(b)):
            arr[l + i] = b[i]

    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)

if __name__ == "__main__":
    n = 9
    arr = [5, 7, 8, 9, 6, 1, 2, 3, 4]
    Solution().mergeSort(arr, 0, n - 1)
    for i in range(n):
        print(arr[i], end=" ")
    print()

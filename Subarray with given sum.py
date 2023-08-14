def subArraySum(arr, n, s):
    current = 0
    left = 0
    right = 0
    while right < n:
        if current == s:
            return [left + 1, right] if left < right else [-1]
        if current < s:
            current += arr[right]
            right += 1
        else:
            current -= arr[left]
            left += 1
    if current == s:
        return [left + 1, right] if left < right else [-1]
    return [-1]


print(subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))
print(subArraySum([1, 2, 3, 7, 5], 5, 12))
print(subArraySum([1, 2, 3, 4], 4, 0))
s = "135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134"
l = [int(x) for x in s.split()]
print(subArraySum(l, 42, 468))

def subArraySum(arr, n, s):
    left = 0
    right = 0
    sum = 0

    while right < n:
        sum += arr[right]

        while s < sum and left < right:
            sum -= arr[left]
            left += 1

        if sum == s:
            return [left + 1, right + 1]

        right += 1

    return [-1]


print(subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))
print(subArraySum([1, 2, 3, 7, 5], 5, 12))
print(subArraySum([1, 2, 3, 4], 4, 0))
s = "135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134"
q = "142 112 54 69 148 45 63 158 38 60 124 142 130 179 117 36 191 43 89 107 41 143 65 49 47 6 91 130 171 151 7 102 194 149 30 24 85 155 157 41 167 177 132 109 145 40 27 124 138 139 119 83 130 142 34 116 40 59 105 131 178 107 74 187 22 146 125 73 71 30 178 174 98 113"
l = [int(x) for x in s.split()]
m = [int(x) for x in q.split()]
print(subArraySum(l, 42, 468))
print(subArraySum(m, 74, 665))

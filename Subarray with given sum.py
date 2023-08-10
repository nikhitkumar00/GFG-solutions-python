def subArraySum(a, n, s):
    start = 0  # Start of the sliding window
    current_sum = 0

    for end in range(n):
        current_sum += a[end]

        while current_sum > s:
            current_sum -= a[start]
            start += 1

        if current_sum == s:
            return start + 1, end + 1

    return -1

print(subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))
print(subArraySum([1, 2, 3, 7, 5], 5, 12))
print(subArraySum([1, 2, 3, 4], 4, 0))

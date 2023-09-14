def maxSum(arr, n):
    arr.sort()
    sum = 0
    for i in range(n // 2):
        sum += 2 * arr[i]
        sum -= 2 * arr[n - i - 1]
    return abs(sum)


n = int(input())
arr = list(map(int, input().split()))
ans = maxSum(arr, n)
print(ans)

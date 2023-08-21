def maxSubarraySum(Arr, N):
    max_ending_here = Arr[0]
    max_so_far = Arr[0]

    for i in range(1, N):
        max_ending_here = max(Arr[i], max_ending_here + Arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

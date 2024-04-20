# User function Template for python3


class Solution:
    def winner(self, arr, n):

        dic = {}
        maxx = 0

        for i in arr:
            dic[i] = 1 if i not in dic else dic[i] + 1
            maxx = max(maxx, dic[i])

        out = sorted([i for i in dic if dic[i] == maxx])

        return [out[0], maxx]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):

        n = int(input())
        arr = input().strip().split()

        result = Solution().winner(arr, n)
        print(result[0], result[1])
# } Driver Code Ends

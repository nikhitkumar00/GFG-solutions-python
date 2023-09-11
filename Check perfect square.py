# User function Template for python3
class Solution:
    def checkPerfectSquare(ob, N):
        if N < 0:
            return 0

        i = 1
        while N > 0:
            N -= i
            i += 2

        return 1 if N == 0 else 0


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.checkPerfectSquare(N))
# } Driver Code Ends

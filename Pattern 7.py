class Solution:
    def printTriangle(self, N):
        for i in range(N):
            print(" " * (N - i - 1) + "*" * (2 * i + 1))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)

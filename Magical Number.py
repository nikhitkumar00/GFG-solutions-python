from typing import List


class Solution:
    def findMagicalNumber(self, N: int, arr: List[int]) -> int:
        for i in range(N):
            if arr[i] == i:
                return arr[i]
        return -1


# {
# Driver Code Starts


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        N = int(input())

        arr = IntArray().Input(N)

        obj = Solution()
        res = obj.findMagicalNumber(N, arr)

        print(res)


# } Driver Code Ends

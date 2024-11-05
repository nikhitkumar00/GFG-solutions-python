# User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        if k <= 0 or not arr:
            return False

        seen = set()

        for i in range(min(k, len(arr))):
            if arr[i] in seen:
                return True
            seen.add(arr[i])

        for i in range(k, len(arr)):
            if arr[i] in seen:
                return True
            seen.add(arr[i])
            seen.remove(arr[i - k])
        return False


# {
# Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if name == "main":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends

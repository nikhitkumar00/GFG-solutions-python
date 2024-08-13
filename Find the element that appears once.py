#User function Template for python3
class Solution:
    def search(self, n, arr):
        for i in range(0, n - 1, 2):
            if arr[i] != arr[i+1]:
                return arr[i]
        return arr[n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.search(n, arr))

# } Driver Code Ends
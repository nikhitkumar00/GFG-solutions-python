#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):

        b.sort()
        out = []
        for i in query:
            
            temp = 0
            left, right = 0, len(b)-1
            
            while left <= right:
                mid = (left + right) // 2
                
                if b[mid] <= a[i]:
                    temp = mid + 1
                    left = mid + 1
                else:
                    right = mid - 1
                    
            out.append(temp)
        
        return out
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends
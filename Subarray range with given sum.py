#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def subArraySum(self,arr, tar):
        out = 0
        dic = {0 : 1}
        pre = 0
        
        for i in arr:
            pre += i
            if pre - tar in dic:
                out += dic[pre - tar]
            
            dic[pre] = 1 if pre not in dic else dic[pre] + 1
        
        return out

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends
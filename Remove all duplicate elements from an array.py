class Solution:	
    def removeDuplicates(self,str):
        out = ""
        for i in str:
            if i not in out:
                out += i
        return out
	    
	    




str = "geeksforgeeks"
ob = Solution()
ans = ob.removeDuplicates(str)
print(ans)
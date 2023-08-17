class Solution:
    def isPossible(self, S):
        dic ={}
        for i in S:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        flag = 2
        for i in dic:
            if dic[i]%2 != 0:
                flag -= 1
                if flag == 0:
                    break
        return 0 if flag == 0 else 1


S = "meayl"
solObj = Solution()
if solObj.isPossible(S):
    print("Yes")
else:
    print("No")

class Solution:
    def deleteMid(self, s, sizeOfStack):
        if sizeOfStack % 2:
            s.pop(sizeOfStack // 2)
        else:
            s.pop(sizeOfStack // 2 - 1)


sizeOfStack = int(input())
myStack = [int(x) for x in input().strip().split()]
ob = Solution()
ob.deleteMid(myStack, sizeOfStack)
while len(myStack) > 0:
    print(myStack[-1], end=" ")
    myStack.pop()
print()

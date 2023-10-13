class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        
        dep = max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        return 1+dep

from collections import defaultdict
from collections import deque
from sys import stdin, stdout
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    if(len(s)==0 or s[0]=="N"):           
        return None

    ip=list(map(str,s.split()))
    
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    q.append(root)                            
    size=size+1 
    
    i=1                                       
    while(size>0 and i<len(ip)):
        currNode=q[0]
        q.popleft()
        size=size-1
        
        currVal=ip[i]
        if(currVal!="N"):
            currNode.left=Node(int(currVal))
            q.append(currNode.left)
            size=size+1
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        if(currVal!="N"):
            currNode.right=Node(int(currVal))
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

s= input()
root = buildTree(s)
res = Solution().maxDepth(root)
print(res)
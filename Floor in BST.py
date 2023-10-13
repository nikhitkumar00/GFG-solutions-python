class Solution:
    def floor(self, root, x):
        prev = None

        while root != None:
            if root.data == x:
                return x
            elif root.data < x:
                prev = root
                root = root.right
            else:
                root = root.left
        return prev.data if prev is not None else -1


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def insert(tree, val):
    if tree == None:
        return Node(val)
    if val < tree.data:
        tree.left = insert(tree.left, val)
    elif val > tree.data:
        tree.right = insert(tree.right, val)
    return tree


n = int(input())
arr = list(map(int, input().split()))
root = None
for k in arr:
    root = insert(root, k)
s = int(input())
obj = Solution()
print(obj.floor(root, s))

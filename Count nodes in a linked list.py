class Solution:
    def getCount(self, head_node):
        count = 0
        while head_node != None:
            count += 1
            head_node = head_node.next
        return count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next


a = LinkedList()
nodes = [1, 2, 3, 4, 5]
for x in nodes:
    node = Node(x)
    a.append(node)
print(Solution().getCount(a.head))

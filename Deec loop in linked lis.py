class Solution:
    def detectLoop(self, head):
        visited = set()
        while head != None:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def loopHere(self, pos):
        if pos == 0:
            return
        walk = self.head
        for i in range(1, pos):
            walk = walk.next
        self.tail.next = walk


for _ in range(int(input())):
    n = int(input())
    LL = LinkedList()
    for i in input().split():
        LL.insert(int(i))
    LL.loopHere(int(input()))
    print(Solution().detectLoop(LL.head))

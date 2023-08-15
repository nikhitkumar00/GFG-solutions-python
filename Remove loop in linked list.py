"""
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val
"""


class Solution:
    def removeLoop(self, head):
        i = 0
        dic = {head: None}
        while head.next != None:
            if head.next in dic:
                head.next = None
                continue
            dic[head.next] = None
            i += 1
            head = head.next


class Node:
    def __init__(self, val):
        self.next = None
        self.data = val


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, num):
        if self.head is None:
            self.head = Node(num)
            self.tail = self.head
        else:
            self.tail.next = Node(num)
            self.tail = self.tail.next

    def isLoop(self):
        if self.head is None:
            return False

        fast = self.head.next
        slow = self.head

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

    def loopHere(self, position):
        if position == 0:
            return

        walk = self.head
        for _ in range(1, position):
            walk = walk.next
        self.tail.next = walk

    def length(self):
        walk = self.head
        ret = 0
        while walk:
            ret += 1
            walk = walk.next
        return ret


n = 3
arr = tuple(int(x) for x in "1 3 4".split())
pos = 2

ll = linkedList()
for i in arr:
    ll.add(i)
ll.loopHere(pos)

Solution().removeLoop(ll.head)

if ll.isLoop() or ll.length() != n:
    print(0)
else:
    print(1)

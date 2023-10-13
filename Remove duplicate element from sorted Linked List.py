def removeDuplicates(head):
    s = set()
    prev = head

    while head is not None:
        if head.data not in s:
            s.add(head.data)
            prev = head
        else:
            prev.next = head.next
        head = head.next


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def printList(self):
        if self.head is None:
            print(" ")
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print("")


n = int(input())
a = LinkedList()
nodes = list(map(int, input().strip().split()))
for x in nodes:
    a.append(x)
removeDuplicates(a.head)
a.printList()

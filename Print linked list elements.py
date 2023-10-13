class Solution:
    def display(self, node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next


class node:
    def __init__(self):
        self.data = None
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


llist = Linked_List()
n = int(input())
values = list(map(int, input().strip().split()))
for i in values:
    llist.insert(i)
Solution().display(llist.get_head())
print("")

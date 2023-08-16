'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    node = 2
    rethead = head
    if k == 1:
        rethead = head.next
    else:
        previous = head
        head = head.next
        while head.next != None:
            if k == node:
                previous.next = head.next
                return rethead
            previous = head
            head = head.next
            node += 1
        if node == k:
            previous.next = None
    return rethead
                

class node:
    def __init__(self):
        self.data = None
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')


list1 = Linked_List()
n = 6
values = [1,2,3,4,5,6]
for i in values:
    list1.insert(i)
k = 6
newhead = delNode(list1.head, k)
printlist(newhead)
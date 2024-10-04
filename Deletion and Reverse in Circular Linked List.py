#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        if head is None or head.next == head:
            return head

        prev = None
        curr = head
        next = None

        while True:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            if curr == head:
                break
        
        head.next = prev
        return prev
        
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        if head is None:
            return None
        
        # Case 1: Deleting the head node
        if head.data == key:
            if head.next == head:
                return None
            
            tail = head
            while tail.next != head:
                tail = tail.next
            
            new_head = head.next
            tail.next = new_head
            return new_head

        # Case 2: Deleting a non-head node
        prev = head
        cur = head.next
        while cur != head:
            if cur.data == key:
                prev.next = cur.next
                return head
            prev = cur
            cur = cur.next
        
        return head
        
        
        #{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends
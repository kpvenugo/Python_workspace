class Node():

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def createLoop(self, position):
        current = self.head
        current_position = 1
        while current.next is not None:
            if current_position == position:
                position_node = current
            current = current.next
            current_position += 1
        current.next = position_node

    def findLoop(self):
        if self.head is None:
            print("Linked List empy")
            return
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer.next and fast_pointer.next.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer == slow_pointer:
                print("loop")
                return
        print("no loop")

    def reverseList(self):
        if self.head is None:
            print("Linked List empy")
            return
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


L1 = LinkedList()
for i in range(10, 9, -1):
    L1.insert(i)

L1.printList()
L1.findLoop()
# L1.createLoop(3)
# L1.findLoop()

L1.reverseList()
L1.printList()

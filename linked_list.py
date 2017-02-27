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

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            current_node = current_node.next
            count += 1
        return count

    def search(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, data):
        if self.head is None:
            print("Empty linked list")
            return 0
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data != data:  # Traverse until data is found
                previous_node = current_node
                current_node = current_node.next
            # data is found in 3 types as follows
            elif previous_node is None:  # data found at first \
                # node ( previous node still is None)
                self.head = current_node.next
                current_node = current_node.next
            elif current_node.next is None:  # data is the last element
                    previous_node.next = None
                    return
            else:  # data found at another position.. detach and reattach next
                previous_node.next = current_node.next
                current_node = previous_node.next

    def getFirstNode(self):
        return self.head

    def reverseUtil(self, current_node, previous_node):
        if current_node.next is None:
            self.head = current_node
            current_node.next = previous_node
            return
        next_node = current_node.next
        current_node.next = previous_node
        self.reverseUtil(next_node, current_node)

    def reverse(self):
        if self.head is None:
            print("list empty")
            return
        self.reverseUtil(self.head, None)

    def printList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return None

    def nonRecursiveReversr(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        if self.head.next is None:
            return
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def reverseKtoM(self, k , m):
        count = 0
        current = self.head
        next = None
        while count < k and current is not None:
            count =+ 1
            current = current.next
        if current is None:
            print("k greater than length of LinkedList")
            return
        reverse_head = current
        reverse_tail = current.next
        previous = current
        while count < m:
            count =+ 1
            next = current.next
            current.next  = previous
            previous = current
            current = current.next
        reverse_head.next = current

L1 = LinkedList()
for i in range(5, 0, -1):
    L1.insert(i)
L1.printList()
print("")
L1.reverse()
L1.printList()
print("")
L1.nonRecursiveReversr()
L1.printList()
# size() the paranthesis is imp otherwise it will print the size method


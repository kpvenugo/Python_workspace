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


L1 = LinkedList()
for i in range(5, 0, -1):
    L1.insert(i)
L1.printList()
print("")
L1.reverse()
L1.printList()
# size() the paranthesis is imp otherwise it will print the size method

import math
import random


class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def recursive_reverseLL(self):
        if self.next is None:
            return self
        self = self.next
        new_head_node = self.recursive_reverseLL()
        self.next.next = self.next
        return new_head_node


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        if self.head is None:
            print("empty List")
            return
        current = self.head
        while current.next is not None:
            print(current.data, end="-->")  # Print till last but one node
            current = current.next
        print(current.data)  # Last node

    def count(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def getNth(self, n):
        if self.count() < n:
            print("n greater than length")
            return
        current = self.head
        count = 1
        while current is not None:
            if count == n:
                return current
            count += 1
            current = current.next
        return None

    def DeleteNth(self, n):
        if n == 1:
            self.head = self.head.next
            return
        if self.count() < n:
            print("n greater than length")
            return None
        current = self.head
        previous = None
        count = 1
        while current is not None:
            if count == n:
                previous.next = current.next
                return
            count += 1
            previous = current
            current = current.next

    def deleteList(self):
        for i in range(1, L1.count() + 1):
            self.DeleteNth(1)

    def pop(self):
        if self.head is None:
            print("Pop error")
        top = self.head
        self.head = self.head.next
        return top

    def insertNth(self, n, data):
        if(n > self.count()):
            print("n larger than length")
            return
        count = 1
        current = self.head
        previous = None
        newNode = Node(data)
        while current is not None:
            if count == n:
                previous.next = newNode
                newNode.next = current
                return
            previous = current
            current = current.next
            count += 1

    def sortedInsert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        previous = None
        while current is not None:
            if new_node.data > current.data:
                previous = current
                current = current.next
                continue
            if previous is None:  # Insert at first
                new_node.next = current
                self.head = new_node
                return
            new_node.next = current  # insert at middle
            previous.next = new_node
            return
        previous.next = new_node  # insert at last

    def append(self, secondList):
        if self.head is None:
            self.head = secondList.head
            return
        if secondList.head is None:
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = secondList.head

    def split(self):  # Split a Linkedlist from mid and return second list
        if self.head is None:
            return None
        length = self.count()
        mid = length / 2  # Note the change with python3(default is float)
        mid = math.ceil(mid)
        print("mid", mid)
        current = self.head
        count = 0
        previous = None
        while count != mid:
            previous = current
            current = current.next
            count += 1
        previous.next = None
        print("previous", previous.data)
        secondList = LinkedList(current)
        return secondList

    def removeDuplicateFromSorted(self):
        if self.head is None:
            return
        current = self.head
        previous = None
        while current is not None:
            if previous is None:
                previous = current
                current = current.next
                continue
            if current.data == previous.data:
                previous.next = current.next
            else:
                previous = current
            current = current.next

    def moveNode(self, fromList):
        if fromList.head is None:
            return
        if self.head is None:
            self.head = fromList.head
            fromList.head = fromList.head.next
            self.head.next = None
            return
        new_head_fromList = fromList.head.next
        fromList.head.next = self.head
        self.head = fromList.head
        fromList.head = new_head_fromList

    def alternateList(self):  # use helper function moveNode
        if self.head is None:
            return None
        count = 1
        listList = []  # to return back 2 lists
        current = self.head
        newList1 = LinkedList()
        newList2 = LinkedList()
        while current is not None:
            current = current.next
            if count % 2 == 1:
                newList1.moveNode(self)
            else:
                newList2.moveNode(self)
            count += 1
        listList.append(newList1)
        listList.append(newList2)
        return listList

    def recursiveReverse(self):
        first_node = self.head
        self.head = first_node.recursive_reverseLL()  # Note this doesn't work

    def shuffleMerge(self, secondList):
        if self.head is None:
            self.head = secondList.head
            return
        if secondList.head is None:
            return
        current = self.head
        next = current.next
        current_second = secondList.head
        next_second = secondList.head.next
        while current.next is not None and current_second.next is not None:
            current.next = current_second
            current_second.next = next
            current = next
            next = current.next
            current_second = next_second
            next_second = current_second.next
        if current.next is None:
            if current_second.next is not None:
                current.next = current_second
        else:
            current.next = current_second
            current_second.next = next


L1 = LinkedList()
L2 = LinkedList()
sList = LinkedList()
# input_list = [5, 612, 3, 23, 32, 1, 25, 6, 28, 414, 19]
for i in range(5, 0, -1):
    L1.insert(2 * i)
for i in range(10, 0, -1):
    L2.insert(2 * i - 1)

L1.printList()
L2.printList()

# # # print("")z
# print(L1.count())
# # L1.insertNth(5, "data")
# L1.printList()
# # #L1.deleteList()
# print(L1.count())
# secondList = L2.split()
# L2.printList()
# print("")
# secondList.printList()

# duplicateList = LinkedList()
# for i in range(15, 0, -1):
#     duplicateList.insert(4)
# duplicateList.insert(2)
# duplicateList.insert(2)
# duplicateList.insert(1)
# duplicateList.insert(1)
# duplicateList.printList()
# print("")
# duplicateList.removeDuplicateFromSorted()
# duplicateList.printList()
# L1.printList()
# listList = L1.alternateList()
# for list in listList:
#     list.printList()

# L1.recursiveReverse()
# L1.printList()
L1.shuffleMerge(L2)
L1.printList()

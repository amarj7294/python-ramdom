import copy
import qwe as q


class Node:

    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while(node):
            print node.value
            node = node.next

    def add(self, newvalue):
        newNode = Node(newvalue)
        # temp = self.head
        # self.head = newNode
        # newNode.next = temp
        newNode.next = self.head
        self.head = newNode

    def addAfter(self, oldnode, newvalue):
        newNode = Node(newvalue)
        node = self.head
        newNode.next = oldnode.next
        oldnode.next = newNode

    def append(self, newvalue):
        newNode = Node(newvalue)
        if self.head is None:
            self.head = newNode
            return
        node = self.head
        while(node.next):
            node = node.next
        node.next = newNode

    def reverse(self):

        current = self.head
        previous = None
        node = None
        # next = None

        while(current):
            # next = current.next
            previous = copy.deepcopy(current)
            previous.next = node
            node = previous
            current = current.next

            ''' next = current.next
            current.next = previous
            previous = current
            current = next'''
        self.head = node
        # self.head = previous


llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)


llist.head.next = second
second.next = third
third.next = fourth
llist.traverse()


'''print("adding a node initial")
addValue = 10
llist.add(addValue)
llist.traverse()'''

'''print("After a node")
addval = 12
after = second
llist.addAfter(after, addval)
llist.traverse()'''


print("End of a node")
addval = 12
llist.append(addval)
llist.traverse()

'''print ("reversing")
llist.reverse()
llist.traverse()'''

q.m()

'''class Queue:
    def __init__(self, maxSize):
        self.queue = list()
        self.maxSize = maxSize
        self.tail = 0
        self.head = 0

    def add(self, data):
        if self.size() >= self.maxSize:
            print "queue full!!!!"
        else:
            self.queue.append(data)
            self.tail += 1
            return True

    def size(self):
        return self.tail - self.head

    def display(self):
        print self.queue[self.head:self.tail]

    def delete(self):
        if self.size() == 0:
            print "queue Empty!"
            self.resetQueue()
        else:
            data = self.queue[self.head]
            self.head += 1
            return data

    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()


q = Queue(8)
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.display()
print(q.delete())
q.display()
'''


class Queue:
    def __init__(self, maxSize):
        self.queue = list()
        self.maxSize = maxSize
        self.tail = 0
        self.head = 0

    def add(self, data):
        print self.size()
        if self.size() == self.maxSize - 1:
            print "queue full!!!!"
        else:
            self.queue.append(data)
            self.tail = (self.tail + 1) % self.maxSize
            # print self.size(), self.maxSize, self.tail, self.head
            return True

    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        return (self.maxSize - (self.head - self.tail))

    def display(self):
        print self.queue[self.head:self.tail]
        print len(self.queue)

    def delete(self):
        if self.size() == 0:
            print "queue Empty!"
        else:
            data = self.queue[self.head]
            self.head = (self.head + 1) % self.maxSize
            print self.size(), self.maxSize, self.tail, self.head
            return data


q = Queue(8)
print(q.add(1))
# q.add(2)
# q.add(3)
# print(q.delete())
# q.add(4)
# q.display()
print(q.add(2))
print(q.add(3))
print(q.add(4))
print(q.add(5))
print(q.add(6))
print(q.add(7))
print(q.add(8))
print(q.add(9))

print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())

print(q.add(1))


# print(q.delete())
# q.display()

# FIFO

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print("enqueued", "added", data)

    # O(N)
    def dequeue(self):
        if len(self.queue) > 0:
            lastItem = self.queue[0]
            del self.queue[0]
            print("dequeued", lastItem)
            return lastItem
        else:
            return -1

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return -1

    def printQueue(self):
        for i in self.queue:
            print(i, end="")
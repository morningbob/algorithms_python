# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Queue import Queue

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.peek()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.printQueue()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

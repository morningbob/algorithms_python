
# FIFO
class Stack:

    def __init__(self):
        # use of arrays as underlying structure
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print("added ", data)

    def pop(self):
        if len(self.stack) > 0:
            lastItem = self.stack[len(self.stack) - 1]
            self.stack.remove(lastItem)
            return lastItem
        else:
            print("There is no item in the stack")
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None


    def printStack(self):
        for i in self.stack:
            print(i, " ", end="")


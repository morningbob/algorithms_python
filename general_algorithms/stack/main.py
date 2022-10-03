# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Stack import Stack





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    #stack.push(4)
    #stack.push(5)
    #stack.push(6)

    print(stack.peek())
    stack.printStack()
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.printStack()



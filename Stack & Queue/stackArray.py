# Implementation of stack using Arrays

class StackArray:

    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Array is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Array is empty")
        else:
            return self.items[-1]

    def display(self):
        if self.is_empty():
            print("Array is empty")
        else:
            print(self.items)

if __name__ == "__main__":

    stack = StackArray()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display()
    stack.pop()
    stack.display()
    print(stack.peek())
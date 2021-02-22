# Implementing Stack using Linked List

class Node:
    def __init__(self, value):
        self.link = None
        self.value = value

class StackLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        if self.is_empty():
            return 0
        else:
            c = 0
            p = self.head
            while p is not None:
                c = c + 1
                p = p.link
            return c

    def push(self, value):
        temp = Node(value)
        temp.link = self.head
        self.head = temp

    def pop(self):
        if self.is_empty():
            print("Array is empty.")
        else:
            value = self.head.value
            self.head = self.head.link
            return value

    def peek(self):
        if self.is_empty():
            print("Array is empty.")
        else:
            return self.head.value

    def display(self):
        s = ()
        if self.is_empty():
            print("Array is empty.")
        else:
            p = self.head
            while p is not None:
                s = s + (p.value,)
                p = p.link

            print(s)


if __name__ == "__main__":

    stack = StackLinkedList()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display() # (4, 3, 2)
    stack.push(5)
    stack.display() # (5, 4, 3, 2)
    print(stack.pop())  # 5
    print(stack.pop())  # 4
    stack.display() # (3, 2)
    print(stack.peek())
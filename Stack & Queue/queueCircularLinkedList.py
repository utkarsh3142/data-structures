# Implementing Queue using Circular Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueCLinkedList:
    def __init__(self):
        self.tail = None

    def is_empty(self):
        return not self.tail

    def size(self):
        if not self.tail:
            return 0
        else:
            c = 0
            p = self.tail.next
            while True:
                c = c + 1
                p = p.next
                if p == self.tail.next:
                    break
        return c

    def enqueue(self, value):
        temp = Node(value)
        if not self.tail:
            self.tail = temp
            self.tail.next = temp
        else:
            temp.next = self.tail.next
            self.tail.next = temp
            self.tail = temp

    def dequeue(self):
        if not self.tail:
            print("Queue is empty.")
        elif self.tail.next == self.tail:
            value = self.tail.value
            self.tail = None
        else:
            value = self.tail.next.value
            self.tail.next = self.tail.next.next
        return value

    def peek(self):
        if not self.tail:
            print("Queue is empty.")
        else:
            return self.tail.next.value

    def display(self):
        if not self.tail:
            print("Queue is empty.")
        else:
            queue_values = ()
            p = self.tail.next
            while True:
                queue_values = queue_values + (p.value,)
                p = p.next
                if p == self.tail.next:
                    break
            print(queue_values)


if __name__ == "__main__":

    queue = QueueCLinkedList()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()
    print("Size: ", queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.display()
    print("Size: ", queue.size())
    print(queue.peek())
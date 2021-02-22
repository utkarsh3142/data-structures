# Implementing Queue using Linked List (Double ended linked list)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def is_empty(self):
        return not self.head

    def size(self):
        return self.queue_size

    def enqueue(self, value):
        temp = Node(value)
        if not self.head:
            self.head = temp
        else:
            self.tail.next = temp
        self.tail = temp
        self.queue_size = self.queue_size + 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            temp = self.head.value
            self.head = self.head.next
            self.queue_size = self.queue_size - 1
            return temp

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            return self.head.value

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            queue_values = ()
            p = self.head
            while p is not None:
                queue_values = queue_values + (p.value,)
                p = p.next
            print(queue_values)


if __name__ == "__main__":

    queue = QueueLinkedList()
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

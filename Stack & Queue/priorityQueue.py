# Implementing Priority Queue

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def enqueue(self, value, priority):
        temp = Node(value, priority)
        if self.is_empty() or priority < self.head.priority:
            temp.next = self.head
            self.head = temp
        else:
            p = self.head
            while p.next is not None and p.priority <= priority:
                p = p.next
            temp.next = p.next
            p.next = temp

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            x = self.head.value
            self.head = self.head.next
            return x

    def size(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            c = 0
            p = self.head
            while p is not None:
                c = c + 1
                p = p.next
        return c

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
    queue = PriorityQueue()
    queue.enqueue(2, 3)
    queue.enqueue(3, 2)
    queue.enqueue(4, 4)
    queue.enqueue(5, 1)
    queue.display()
    print("Size: ", queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.display()
    print("Size: ", queue.size())
    print(queue.peek())
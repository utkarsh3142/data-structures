# Implementing Circular Queue using Arrays

class CircularQueue:
    def __init__(self, queue_size=10):
        self.items = [None] * queue_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return len(self.items) - self.front == 0

    def resize(self, new_queue_size):
        old_items = self.items
        self.items = [] * new_queue_size
        i = self.front
        for j in range(self.count):
            self.items[j] = old_items[i]
            i = (i + 1) % len(old_items)
        self.front = 0

    def size(self):
        return self.count

    def enqueue(self, value):
        if self.count == len(self.items):
            self.resize(2*len(self.items))

        i = (self.front + self.count) % len(self.items)
        self.items[i] = value
        self.count = self.count + 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            x = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % len(self.items)
            self.count = self.count + 1
            return x

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            return self.items[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(self.items)

if __name__ == "__main__":

    queue = CircularQueue(5)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.display()
    print(queue.peek())

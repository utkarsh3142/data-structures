# Implementing Queue using Array (& incrementing front index based on Dequeue operation)

class QueueArray:
    def __init__(self):
        self.items = []
        self.front = 0

    def is_empty(self):
        return len(self.items) - self.front == 0

    def size(self):
        return len(self.items) - self.front

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            x = self.items[self.front]
            self.items[self.front] = None
            self.front = self.front + 1
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

    queue = QueueArray()
    print(queue.size())
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.display()
    print(queue.dequeue())
    queue.display()
    print(queue.dequeue())
    print(queue.peek())
    queue.display()

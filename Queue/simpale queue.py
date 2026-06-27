# Simple Queue using List

class Queue:
    def __init__(self):
        self.queue = []

    # Add element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove element
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
            return
        return self.queue.pop(0)

    # Front element
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
            return
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)


# Driver Code
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:")
q.display()

print("Front:", q.peek())

print("Dequeued:", q.dequeue())

print("Queue After Dequeue:")
q.display()

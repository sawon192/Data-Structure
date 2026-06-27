import heapq

# Priority Queue using Heap

class PriorityQueue:
    def __init__(self):
        self.items = []

    # Insert an element
    def enqueue(self, value):
        heapq.heappush(self.items, value)

    # Remove highest priority element
    def dequeue(self):
        if len(self.items) == 0:
            print("Priority Queue is Empty")
            return

        return heapq.heappop(self.items)

    # Show highest priority element
    def peek(self):
        if len(self.items) == 0:
            print("Priority Queue is Empty")
            return

        return self.items[0]

    # Display all elements
    def display(self):
        print(self.items)


# Driver Program
pq = PriorityQueue()

pq.enqueue(15)
pq.enqueue(8)
pq.enqueue(25)
pq.enqueue(3)
pq.enqueue(12)

print("Priority Queue:")
pq.display()

print("Front Element:", pq.peek())

print("Deleted Element:", pq.dequeue())

print("Priority Queue after Deletion:")
pq.display()

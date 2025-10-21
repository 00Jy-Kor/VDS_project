class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return "Queue: " + str(self.items)
    
    def reset(self):
        self.items = []

#test
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)  # Queue: [1, 2, 3]
    print("Dequeue:", queue.dequeue())  # Dequeue: 1
    print("Front:", queue.front())  # Front: 2
    print("Is Empty:", queue.is_empty())  # Is Empty: False
    print("Size:", queue.size())  # Size: 2
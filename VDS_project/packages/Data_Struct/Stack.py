class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return "Stack: " + str(self.items)
    
    def reset(self):
        self.items = []

#test
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)  # Stack: [1, 2, 3]
    print("Pop:", stack.pop())  # Pop: 3
    print("Peek:", stack.peek())  # Peek: 2
    print("Is Empty:", stack.is_empty())  # Is Empty: False
    print("Size:", stack.size())  # Size: 2
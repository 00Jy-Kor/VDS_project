class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def peek(self):
        return self.heap[0] if self.heap else None
    
    def inorder(self):
        return sorted(self.heap)
    
    def reset(self):
        self.heap = []
    
class MinHeap(BinaryHeap):
    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    
    def heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)
    
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_value
    
class MaxHeap(BinaryHeap):
    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    
    def heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)
    
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_value

#min heap test
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(30)
    heap.insert(25)
    
    print("Heap Inorder Traversal:", heap.inorder())  # 힙 요소 정렬된 형태 출력
    print("Extract Min:", heap.extract_min())  # 최소값 추출
    print("Heap after extraction:", heap.inorder())
    '''
    Heap Inorder Traversal: [5, 10, 20, 25, 30]
    Extract Min: 5
    Heap after extraction: [10, 20, 25, 30]
    '''
#max heap test
if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(30)
    heap.insert(25)
    
    print("Heap Inorder Traversal:", heap.inorder())  # 힙 요소 정렬된 형태 출력
    print("Extract Max:", heap.extract_max())  # 최대값 추출
    print("Heap after extraction:", heap.inorder())
    '''
    Heap Inorder Traversal: [5, 10, 20, 25, 30]
    Extract Max: 30
    Heap after extraction: [5, 10, 20, 25]
    '''
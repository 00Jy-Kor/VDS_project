class Node:
    def __init__(self, value, height=None, color=None):
        self.value = value
        self.left = None
        self.right = None

        # AVL
        self.height = height

        # rb
        self.color = color
        self.parent = None    

#전위 순회 (preorder) : 루트 → 왼쪽 → 오른쪽
#중위 순회 (inorder) : 왼쪽 → 루트 → 오른쪽
#후위 순회 (postorder) : 왼쪽 → 오른쪽 → 루트

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
    
    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
    
    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
    
    def preorder(self):
        result = []
        self.preorder_traversal(self.root, result)
        return result
    
    def inorder(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result
    
    def postorder(self):
        result = []
        self.postorder_traversal(self.root, result)
        return result

# BinaryTree test
# if __name__ == "__main__":
#     tree = BinaryTree(1)
#     tree.root.left = Node(2)
#     tree.root.right = Node(3)
#     tree.root.left.left = Node(4)
#     tree.root.left.right = Node(5)
    
#     print("Preorder Traversal:", tree.preorder())  # [1, 2, 4, 5, 3]
#     print("Inorder Traversal:", tree.inorder())   # [4, 2, 5, 1, 3]
#     print("Postorder Traversal:", tree.postorder()) # [4, 5, 2, 3, 1]

#완전이진트리
class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def insert_cycle(self, node, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self.insert_cycle(node.left, value)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    self.insert_cycle(node.right, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_cycle(self.root, value)
    
    def search_cycle(self, node, value):
        if node is None or node.value == value:
            return node is not None
        elif value < node.value:
            return self.search_cycle(node.left, value)
        else:
            return self.search_cycle(node.right, value)

    def search(self, value):
        return self.search_cycle(self.root, value)
    
    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def delete_cycle(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self.delete_cycle(node.left, value)
        elif value > node.value:
            node.right = self.delete_cycle(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_larger_node = self.find_min(node.right)
            node.value = min_larger_node.value
            node.right = self.delete_cycle(node.right, min_larger_node.value)
        
        return node
    
    def delete(self, value):
        self.root = self.delete_cycle(self.root, value)
    
    def reset(self):
        self.root = None
        

# BST test
# if __name__ == "__main__":
#     bst = BinarySearchTree()
#     bst.insert(5)
#     bst.insert(3)
#     bst.insert(7)
#     bst.insert(2)
#     bst.insert(4)
#     bst.insert(6)
#     bst.insert(8)
    

#     print("preorder Traversal:",    bst.preorder())  # [5, 3, 2, 4, 7, 6, 8]
#     print("Search 4:", bst.search(4))  # True
#     print("Search 10:", bst.search(10))  # False
#     bst.delete(3)
#     print("preorder After Deletion:", bst.preorder())  # [5, 4, 2, 7, 6, 8]

#자가균형이진탐색트리 수정필요
class AVLTree(BinaryTree):
    def __init__(self):
        self.root = None
    
    def height(self, node):
        return node.height if node else 0
    
    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0
    
    def rotate_right(self, y):
        x = y.left
        T = x.right
        x.right = y
        y.left = T
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    def rotate_left(self, x):
        y = x.right
        T = y.left
        y.left = x
        x.right = T
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y
    
    def balance(self, node):
        balance = self.balance_factor(node)
        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    
    def insert_cycle(self, node, value):
        if not node:
            return Node(value, 1)
        if value < node.value:
            node.left = self.insert_cycle(node.left, value)
        else:
            node.right = self.insert_cycle(node.right, value)
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return self.balance(node)
    
    def insert(self, value):
        self.root = self.insert_cycle(self.root, value)

    def find_min(self, node):
            while node.left:
                node = node.left
            return node
    
    def delete_cycle(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self.delete_cycle(node.left, value)
        elif value > node.value:
            node.right = self.delete_cycle(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_larger_node = self.find_min(node.right)
            node.value = min_larger_node.value
            node.right = self.delete_cycle(node.right, min_larger_node.value)
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return self.balance(node)
    
    def delete(self, value):
        self.root = self.delete_cycle(self.root, value)    

    def reset(self):
        self.root = None

# AVL test
# if __name__ == "__main__":
#     avl = AVLTree()
#     avl.insert(10)
#     avl.insert(20)
#     avl.insert(30)
#     avl.insert(40)
#     avl.insert(50)
#     avl.insert(25)
    
#     print("preorder Traversal:", avl.preorder())  # [30, 20, 10, 25, 40, 50]
#     avl.delete(30)
#     print("preorder After Deletion:", avl.preorder()) # [40, 20, 10, 25, 50]

#레드블랙트리
class RedBlackTree(BinaryTree):
    RED = "RED"
    BLACK = "BLACK"

    def __init__(self, root_value=None):
        self.NIL = Node(value=None, color=RedBlackTree.BLACK) 
        self.root = self.NIL
        if root_value is not None:
            self.insert(root_value)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        new_node = Node(key, color=RedBlackTree.RED)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = RedBlackTree.BLACK
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, k):
        while k.parent and k.parent.color == RedBlackTree.RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right  # uncle
                if u and u.color == RedBlackTree.RED:
                    # case 1: uncle is red
                    u.color = RedBlackTree.BLACK
                    k.parent.color = RedBlackTree.BLACK
                    k.parent.parent.color = RedBlackTree.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # case 2: triangle
                        k = k.parent
                        self.left_rotate(k)
                    # case 3: line
                    k.parent.color = RedBlackTree.BLACK
                    k.parent.parent.color = RedBlackTree.RED
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left  # uncle
                if u and u.color == RedBlackTree.RED:
                    u.color = RedBlackTree.BLACK
                    k.parent.color = RedBlackTree.BLACK
                    k.parent.parent.color = RedBlackTree.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = RedBlackTree.BLACK
                    k.parent.parent.color = RedBlackTree.RED
                    self.left_rotate(k.parent.parent)

            if k == self.root:
                break
        self.root.color = RedBlackTree.BLACK

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, key):
        z = self.root
        while z != self.NIL and z.value != key:
            if key < z.value:
                z = z.left
            else:
                z = z.right

        if z == self.NIL:
            print("값을 찾을 수 없습니다:", key)
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == RedBlackTree.BLACK:
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == RedBlackTree.BLACK:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == RedBlackTree.RED:
                    s.color = RedBlackTree.BLACK
                    x.parent.color = RedBlackTree.RED
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == RedBlackTree.BLACK and s.right.color == RedBlackTree.BLACK:
                    s.color = RedBlackTree.RED
                    x = x.parent
                else:
                    if s.right.color == RedBlackTree.BLACK:
                        s.left.color = RedBlackTree.BLACK
                        s.color = RedBlackTree.RED
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = RedBlackTree.BLACK
                    s.right.color = RedBlackTree.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == RedBlackTree.RED:
                    s.color = RedBlackTree.BLACK
                    x.parent.color = RedBlackTree.RED
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == RedBlackTree.BLACK and s.left.color == RedBlackTree.BLACK:
                    s.color = RedBlackTree.RED
                    x = x.parent
                else:
                    if s.left.color == RedBlackTree.BLACK:
                        s.right.color = RedBlackTree.BLACK
                        s.color = RedBlackTree.RED
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = RedBlackTree.BLACK
                    s.left.color = RedBlackTree.BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = RedBlackTree.BLACK

    def preorder_traversal(self, node, result):
            if node != self.NIL and node is not None:
                result.append((node.value, node.color))
                self.preorder_traversal(node.left, result)
                self.preorder_traversal(node.right, result)
                
    def preorder(self):
        result = []
        self.preorder_traversal(self.root, result)
        return result
    
    def inorder_traversal(self, node, result):
        if node != self.NIL and node is not None:
            self.inorder_traversal(node.left, result)
            result.append((node.value, node.color))
            self.inorder_traversal(node.right, result)
    
    def inorder(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result
    
    def postorder_traversal(self, node, result):
        if node != self.NIL and node is not None:
                self.postorder_traversal(node.left, result)
                self.postorder_traversal(node.right, result)
                result.append((node.value, node.color))

    def postorder(self):
        result = []
        self.postorder_traversal(self.root, result)
        return result
    
    def reset(self):
        self.root = None

# RbTree Test
# if __name__ == "__main__":
#     rbt = RedBlackTree()
#     rbt.insert(10)
#     rbt.insert(20)
#     rbt.insert(30)
#     rbt.insert(40)
#     rbt.insert(50)
#     rbt.insert(25)
  
#     print("preorder Traversal:", rbt.preorder()) # [(20, 'BLACK'), (10, 'BLACK'), (40, 'RED'), (30, 'BLACK'), (25, 'RED'), (50, 'BLACK')]

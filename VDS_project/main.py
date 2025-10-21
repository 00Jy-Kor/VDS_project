#import
import pygame
import pygame_gui
from enum import Enum, auto

# My class
from UI import UI
from packages.Data_Struct import Stack, Queue, Node, BinarySearchTree, AVLTree, RedBlackTree, MinHeap, MaxHeap

class Mode(Enum):
    basis = auto()
    Stack = auto()
    Queue = auto()
    Bst = auto()
    Avl = auto()
    Rb = auto()
    Heap = auto()

# used color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)

# pygame 초기화
pygame.init()

# font
font = pygame.font.Font(None, 25)

# window setting
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Visible Data Struct")

screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)

# time
clock = pygame.time.Clock()

# UI
ui_manager = pygame_gui.UIManager((screen_size), "Ui.json")
ui = UI(ui_manager)

# DataStruct
stack = Stack()
queue = Queue()
bst = BinarySearchTree()
avl = AVLTree()
rb = RedBlackTree()
minheap = MinHeap()
maxheap = MaxHeap()

# Funtion
def drow_stack():
    box_size = (130, 50) 

    for index, value in enumerate(stack.items):
        x = int(WIDTH / 2.5)
        y = 300 - 50 * index
        point = (x, y)
        box = pygame.Rect(point, box_size)

        pygame.draw.rect(screen, LIGHT_BLUE, box)
        pygame.draw.rect(screen, BLACK, box, width=3)

        label = font.render(str(value), True, BLACK)
        text_rect = label.get_rect(center=box.center)
        screen.blit(label, text_rect)

def drow_qeueue():
    box_size = (50, 50)

    for index, value in enumerate(queue.items):
        x = int(WIDTH / 4) + 50 * index
        y = 300
        point = (x, y)
        box = pygame.Rect(point, box_size)

        pygame.draw.rect(screen, LIGHT_BLUE, box)
        pygame.draw.rect(screen, BLACK, box, width=3)

        label = font.render(str(value), True, BLACK)
        text_rect = label.get_rect(center=box.center)
        screen.blit(label, text_rect)

rootx = WIDTH // 2
rooty = 100
def drow_tree(node, x, y, level):
    interval = 100
    radius = 25

    if node:
        if node.left:
            pygame.draw.line(screen, BLACK, (x, y), (x - interval // level, y + interval), 2)  
            drow_tree(node.left, x - interval // level, y + interval, level + 1) 
        if node.right:
            pygame.draw.line(screen, BLACK, (x, y), (x + interval // level, y + interval), 2)  
            drow_tree(node.right, x + interval // level, y + interval, level + 1)

        pygame.draw.circle(screen, LIGHT_BLUE, (x, y), radius)
        font = pygame.font.Font(None, radius)
        label = font.render(str(node.value), True, BLACK)

        text_rect = label.get_rect(center=(x, y))
        screen.blit(label, text_rect)

def drow_rbtree(node, x, y, level):
    interval = 100
    radius = 25

    if node and node.value is not None:
        if node.left and node.left.value is not None:
            pygame.draw.line(screen, BLACK, (x, y), (x - interval // level, y + interval), 2)  
            drow_rbtree(node.left, x - interval // level, y + interval, level + 1) 
        if node.right and node.right.value is not None:
            pygame.draw.line(screen, BLACK, (x, y), (x + interval // level, y + interval), 2)  
            drow_rbtree(node.right, x + interval // level, y + interval, level + 1)

        if node.color == "BLACK" :
            pygame.draw.circle(screen, BLACK, (x, y), radius)
        elif node.color == "RED":
            pygame.draw.circle(screen, RED, (x, y), radius) 

        font = pygame.font.Font(None, radius)
        label = font.render(str(node.value), True, WHITE)

        text_rect = label.get_rect(center=(x, y)) 
        screen.blit(label, text_rect) 

def build_tree_preorder(values, index=0):
    if index >= len(values):
        return None
    
    node = Node(values[index])
    # 왼쪽 자식 index: 2*index+1
    # 오른쪽 자식 index: 2*index+2
    node.left = build_tree_preorder(values, 2 * index + 1)
    node.right = build_tree_preorder(values, 2 * index + 2)
    return node
     

def main():
    type = Mode.basis
    next_type = Mode.basis
    mode_change = False
    heap = True

    screen.fill(WHITE)
    running = True

    while running:
        time_delta = clock.tick(60) / 1000

        if mode_change:
            screen.fill(WHITE)
            if type == Mode.Stack:
                ui.B_Stack.set_state(False)
                ui.TextEntry1.handle.hide()
                ui.Button.handle.hide()
                stack.reset()

            if type == Mode.Queue:
                ui.B_Queue.set_state(False)
                ui.TextEntry1.handle.hide()
                ui.Button.handle.hide() 
                queue.reset()

            if type == Mode.Bst:
                ui.B_Bst.set_state(False)
                ui.TextEntry1.handle.hide()
                ui.TextEntry2.handle.hide()
                bst.reset()

            if type == Mode.Avl:
                ui.B_Avl.set_state(False)
                ui.TextEntry1.handle.hide()
                ui.TextEntry2.handle.hide()
                avl.reset()

            if type == Mode.Rb:
                ui.B_Rb.set_state(False)
                ui.TextEntry1.handle.hide()
                ui.TextEntry2.handle.hide()
                rb.reset()

            if type == Mode.Heap:
                ui.B_Heap.set_state(False)
                ui.TextEntry1.handle.hide()
                ui.Button.handle.hide() 
                minheap.reset()
                maxheap.reset()
            type = next_type
                        
            if type == Mode.Stack:
                ui.B_Stack.set_state(True)
                ui.TextEntry1.change_name("Push")
                ui.Button.change_name("Pop")
                ui.TextEntry1.handle.show()
                ui.Button.handle.show()

            if type == Mode.Queue:
                ui.B_Queue.set_state(True)
                ui.TextEntry1.change_name("Enqueue")
                ui.Button.change_name("Dequeue")
                ui.TextEntry1.handle.show()
                ui.Button.handle.show()

            if type == Mode.Bst:
                ui.B_Bst.set_state(True)
                ui.TextEntry1.change_name("Insert")
                ui.TextEntry2.change_name("Delete")
                ui.TextEntry1.handle.show()
                ui.TextEntry2.handle.show()

            if type == Mode.Avl:
                ui.B_Avl.set_state(True)
                ui.TextEntry1.change_name("Insert")
                ui.TextEntry2.change_name("Delete")
                ui.TextEntry1.handle.show()
                ui.TextEntry2.handle.show()

            if type == Mode.Rb:
                ui.B_Rb.set_state(True)
                ui.TextEntry1.change_name("Insert")
                ui.TextEntry2.change_name("Delete")
                ui.TextEntry1.handle.show()
                ui.TextEntry2.handle.show()

            if type == Mode.Heap:
                ui.B_Heap.set_state(True)
                ui.TextEntry1.change_name("Insert")
                ui.TextEntry1.handle.show()
                ui.Button.change_name("Max")
                ui.Button.handle.show()

            mode_change = False

        for event in pygame.event.get():
            ui_manager.process_events(event)
            
            #region Exit
            if event.type == pygame.QUIT:
                running = False
            #endregion Exit
            
            #region Event_Button
            if event.type == pygame_gui.UI_BUTTON_PRESSED:

                #Mode change button
                if event.ui_element in (ui.B_Stack.handle, ui.B_Queue.handle, ui.B_Bst.handle, ui.B_Avl.handle, ui.B_Rb.handle, ui.B_Heap.handle):
                    mode_change = True

                    if event.ui_element == ui.B_Stack.handle:
                        if type != Mode.Stack:
                            next_type = Mode.Stack

                    if event.ui_element == ui.B_Queue.handle:
                        if type != Mode.Queue:
                            next_type = Mode.Queue

                    if event.ui_element == ui.B_Bst.handle: 
                        if type != Mode.Bst:
                            next_type = Mode.Bst
                            
                    if event.ui_element == ui.B_Avl.handle:
                        if type != Mode.Avl:
                            next_type = Mode.Avl

                    if event.ui_element == ui.B_Rb.handle:
                        if type != Mode.Rb:
                            next_type = Mode.Rb

                    if event.ui_element == ui.B_Heap.handle:
                        if type != Mode.Heap:
                            next_type = Mode.Heap
                    
                    continue

                #Funtion button
                if event.ui_element == ui.Button.handle:
                    if type == Mode.Stack:
                        if stack.is_empty() != True:
                            stack.pop()
                            screen.fill(WHITE)
                            drow_stack()

                    if type == Mode.Queue:
                        if queue.is_empty() != True:
                            queue.dequeue()
                            screen.fill(WHITE)
                            drow_qeueue()

                    if type == Mode.Heap:
                        screen.fill(WHITE)
                        if heap:
                            heap = False
                            minheap.reset()
                        else:
                            heap = True
                            maxheap.reset()

                        if heap:
                            ui.Button.change_name("Max")
                        else:
                            ui.Button.change_name("Min")


            #endregion Event_Button
            
            #region Event_Text entry Push
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:

                if event.ui_element == ui.TextEntry1.handle:
                    if event.text.strip().isdigit():
                        if type == Mode.Stack:
                                stack.push(event.text)
                                drow_stack()

                        if type == Mode.Queue:
                                queue.enqueue(event.text)
                                drow_qeueue()

                        if type == Mode.Bst:
                                bst.insert(int(event.text))
                                drow_tree(bst.root,rootx, rooty, 1)
                        
                        if type == Mode.Avl:
                                avl.insert(int(event.text))
                                screen.fill(WHITE)
                                drow_tree(avl.root,rootx, rooty, 1)

                        if type == Mode.Rb:
                                rb.insert(int(event.text))
                                screen.fill(WHITE)
                                drow_rbtree(rb.root,rootx, rooty, 1)
                        
                        if type == Mode.Heap:
                            if heap:
                                minheap.insert(int(event.text))
                                screen.fill(WHITE)
                                drow_tree(build_tree_preorder(minheap.heap),rootx, rooty, 1)
                            else:
                                maxheap.insert(int(event.text))
                                screen.fill(WHITE)
                                drow_tree(build_tree_preorder(maxheap.heap),rootx, rooty, 1)
                            

                    ui.TextEntry1.handle.set_text('')
                    ui.TextEntry1.handle.unfocus()
                    ui.TextEntry1.handle.focus()
                
                if event.ui_element == ui.TextEntry2.handle:
                    if event.text.strip().isdigit():
                        if type == Mode.Bst:
                                if bst.search(int(event.text)):
                                    bst.delete(int(event.text))
                                    screen.fill(WHITE)
                                    drow_tree(bst.root,rootx, rooty, 1)
                        
                        if type == Mode.Avl:
                                avl.delete(int(event.text))
                                screen.fill(WHITE)
                                drow_tree(avl.root,rootx, rooty, 1)
                        
                        if type == Mode.Rb:
                                rb.delete(int(event.text))
                                screen.fill(WHITE)
                                drow_rbtree(rb.root,rootx, rooty, 1)

                    ui.TextEntry2.handle.set_text('')
                    ui.TextEntry2.handle.unfocus()
                    ui.TextEntry2.handle.focus()
            #endregion Event_Text entry Push

        ui_manager.update(time_delta)

        ui_manager.draw_ui(screen)

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

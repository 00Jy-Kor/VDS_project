from packages.UI_Element import B_Mode_Trigger, B_Small_Button, Text_Entry

import pygame
import pygame_gui
from pygame_gui.core import ObjectID


class UI:

    def __init__(self, _ui_manager):
        # 모드 선택 버튼
        self.B_Stack = B_Mode_Trigger(_ui_manager, (0, 0), "Stack")
        self.B_Queue = B_Mode_Trigger(_ui_manager, (134, 0), "Queue")
        self.B_Bst = B_Mode_Trigger(_ui_manager, (268, 0), "Bst")
        self.B_Avl = B_Mode_Trigger(_ui_manager, (402, 0), "Avl")
        self.B_Rb = B_Mode_Trigger(_ui_manager, (536, 0), "Rb")
        self.B_Heap = B_Mode_Trigger(_ui_manager, (670, 0), "Heap")

        #버전업
        self.TextEntry1 = Text_Entry(_ui_manager, (20, 50), "None")
        self.TextEntry2 = Text_Entry(_ui_manager, (110, 50), "None")
        self.Button = B_Small_Button(_ui_manager, (110, 50), "None")
        self.TextEntry1.handle.hide()
        self.TextEntry2.handle.hide()
        self.Button.handle.hide()


import pygame
import pygame_gui

Text_entry_size = (80, 20)
class Text_Entry:
    def __init__(self, _ui_manager, _point, _placeholder_text):
        self.handle = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(_point, Text_entry_size),
        manager = _ui_manager,
        placeholder_text = _placeholder_text)

    def change_name(self, _name):
        self.handle.placeholder_text = _name
        self.handle.rebuild()
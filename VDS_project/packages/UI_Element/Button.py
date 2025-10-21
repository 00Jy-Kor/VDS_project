import pygame
import pygame_gui
from pygame_gui.core import ObjectID

class Button:
    def __init__(self, _ui_manager, _point, _button_size):
        rect = pygame.Rect(_point, _button_size)

        self.handle = pygame_gui.elements.UIButton(
        relative_rect = rect,
        manager = _ui_manager,)
    
    def change_name(self, _name):
        self.handle.set_text(_name)

mode_trigger_button_size = (130, 50)
class B_Mode_Trigger(Button):
    def __init__(self, _ui_manager, _point, _name):
        rect = pygame.Rect(_point, mode_trigger_button_size)
        
        self.state = False

        self.handle = pygame_gui.elements.UIButton(
        relative_rect = rect,
        text = _name,
        manager = _ui_manager,
        object_id = ObjectID(object_id="#idle_button"))

    def update(self):
        if self.state == True:
            self.handle.change_object_id(ObjectID(object_id="#selected_button"))
        elif self.state == False:
            self.handle.change_object_id(ObjectID(object_id="#idle_button"))

    def set_state(self, _bool):
        self.state = _bool
        self.update()

b_small_button_size = (40, 20)
class B_Small_Button(Button):
    def __init__(self, _ui_manager, _point, _name):
        rect = pygame.Rect(_point, b_small_button_size)

        self.handle = pygame_gui.elements.UIButton(
        relative_rect = rect,
        text = _name,
        manager = _ui_manager,
        object_id = ObjectID(object_id="#small_button"))
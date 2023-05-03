import pygame
from .Button import Button

class RectangleButton(Button):

    def __init__(self,coords):
        super().__init__(coords, 65, 65)
        self.value = 1

    def draw(self, screen):
        if self.selected:
            self.border = 0
        else:
            self.border = 3
        pygame.draw.rect(screen,(208,31,213), pygame.Rect(self.x , self.y, self.width, self.height), self.border)
        pygame.draw.rect(screen, (0,255, 5),  pygame.Rect(self.x+10 , self.y+10, self.width-20, self.height-20), self.border)
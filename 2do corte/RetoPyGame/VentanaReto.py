import pygame
import sys
from hulk import Hulk
from ironMan import IronMan
class SuperHeroes:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (800, 500) )
        pygame.display.set_caption("Galaga Pirata")
        self.color = (230,230,230)

        self.hulk = Hulk(self)
        self.ironMan = IronMan(self)
        self.hulk = Hulk(self)
        self.hulk = Hulk(self)

    def corre_juego (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill(self.color)

                self.hulk.corre()
                self.ironMan.corre()

            pygame.display.flip()


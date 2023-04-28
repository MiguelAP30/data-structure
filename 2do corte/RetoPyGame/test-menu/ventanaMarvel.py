import pygame
import sys
from menu import Menu
pygame.init()

class Marvel:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Superheroes")
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (134, 181, 129)
        self.RED = (255, 0,   0)
        self.BLUE = (0, 0, 255)
        self.GRAY = (170, 170, 170)
        self.LIGHT_BLUE = (161, 163, 212)
        self.main_menu = Menu(self.screen, {"SLL": "test-menu/imgs/list-outline.png", "DLL": "test-menu/imgs/list-outline.png", "Pilas y colas": "test-menu/imgs/list-outline.png", "Árboles": "test-menu/imgs/tree-solid.png", "Grafos": "test-menu/imgs/circle-nodes-solid.png"}, self.GREEN, 40, "Arial", 22, self.BLACK)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            self.screen.fill(self.WHITE)
            if(self.main_menu.getSelectedOption() == 0):
                pygame.draw.rect(self.screen, (200, 200, 200), (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
                self.drawFooter()               
            elif(self.main_menu.getSelectedOption() == 1):
                pygame.draw.rect(self.screen, (250, 10, 20), (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
            self.main_menu.draw()
            pygame.display.flip()
            
    def dibujarImagenes(self, img, x, y):
        rect= pygame.draw.rect(self.screen, self.white, (x,y,130, 124),0,10)
        self.screen.blit(img, (x,y))
        rect= pygame.draw.rect(self.screen, self.black, (x,y,130, 124),2,10)
        if rect.collidepoint(pygame.mouse.get_pos()):
            rect= pygame.draw.rect(self.screen, self.black, (x, y, 130, 124),2,10)

    def mostrarTexto(self, texto, color, dimensiones, x , y):
        superficie= pygame.font.SysFont("Sans Serif", dimensiones)
        text_surface= superficie.render(texto, True, color)
        self.screen.blit(text_surface, (x,y))

    def drawFooter(self):
        logogit= pygame.image.load("test-menu/imgs/logouam.jpg").convert()
        logogit= pygame.transform.scale(logogit,(55,50))
        
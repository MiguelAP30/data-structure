import pygame
from MenuPanel import MenuPanel
from SingleLinkedListPanel import SLLPanel
from temp_panel import tempPanel
from PilasYColas import Pilas
import sys
class Window:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,700))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.font = pygame.font.SysFont("algerian",20)
        self.cartas = Pilas()
        self.Panel_SLL = SLLPanel(self.font)
        self.temppanel = tempPanel()
        self.Panel_actual = self.Panel_SLL
        self.run_window()

    def run_window(self):
        menu_panel = MenuPanel()

        run = True
        while run:

            ubi_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.Cambio_panel_Actual(menu_panel.click_event(ubi_mouse))
                    self.Panel_actual.click_event(ubi_mouse)
            
            self.screen.fill((100,10,10))
            self.Panel_actual.draw_panel(self.screen, ubi_mouse)
            menu_panel.draw_menu_panel(self.screen, ubi_mouse)
            pygame.display.update()
        

    def Cambio_panel_Actual(self, panel_name):
        if panel_name == "Single Linked List":
            self.Panel_actual = self.Panel_SLL
        elif panel_name == "Double Linked List":
            self.Panel_actual = self.temppanel
        elif panel_name == "Pilas y Colas":
            self.cartas.run()
            self.Panel_actual = self.temppanel
        elif panel_name == "Arboles":
            self.Panel_actual = self.temppanel
        elif panel_name == "Grafos":
            self.Panel_actual = self.temppanel
    

init = Window()
init.run_window()
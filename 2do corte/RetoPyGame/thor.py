import pygame
class IronMan:
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = a_game.screen. get_rect ()
        self.image = pygame.image.load ("RetoPyGame\Imagenes\descarga.jpg")
        self.image = pygame.transform.scale(self.image,(120,120))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def corre(self) :
        self.screen.blit(self.image, self.rect)
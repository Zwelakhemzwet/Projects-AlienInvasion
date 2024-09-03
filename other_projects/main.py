import pygame
from settings import Settings
from buttons import Button

class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1500, 500))
        self.settings = Settings()
    
    def run(self):
        while True:
            self._update_screen()
    
    def _create_button(self):
        self.button1 = Button(self)
    
    def _update_screen(self):
        self.screen.fill(230, 230, 230)
        pygame.display.flip()
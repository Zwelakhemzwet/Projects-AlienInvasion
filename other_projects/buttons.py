import pygame

class Button:
    def __init__(self, Game):
        self.screen = Game.screen
        self.settings = Game.settings
        self.width = self.settings.button_width
        self.height = self.settings.button_height
        self.color = self.settings.button_color
        self.bg_color = (169, 157, 5)

        self.font_color = (246, 245, 240)
        self.font = pygame.font.SysFont(None, 20)

        self.rect = pygame.Rect(0,0, self.width, self.height)
    
    def draw(self):
        self.screen.fill(self.color, self.rect)
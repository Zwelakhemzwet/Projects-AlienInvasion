import pygame

class Ship():
    """класс для управления корабля"""
    def __init__(self, ai_game):
        """инициализует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        #флаг перемещения
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #обновление атрибута x вместо rect
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #обновление атрибута rect на основании self.x
        self.rect.x = self.x
    
    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)


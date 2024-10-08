import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """"класс для управлеия русурсами и поведением игры"""

    def __init__(self):
        """ининциализирует игру и создает игровое ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        #назначение цвета фона
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
    
    def run_game(self):
        """запуст основного цикла игры"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            #при каждом  проходе цикла перерисовывается экран
            self._update_screen()
            

    def _check_events(self):
        """обрабатывает нажатия клавищ и события мыши"""
        #отслеживание событиий клавиатурии и мыши
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
     
    def _check_keydown_events(self, event):
        """реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            #переместить корабль вправо
            self.ship.moving_right = True
        
        elif event.key == pygame.K_LEFT:
            #переместить корабль влево
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """обновляет позиции снарядов и удаляет старые снаряды"""
        #удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _create_fleet(self):
        """создание флота вторжения"""
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        """обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.settings.big_color)
        self.ship.blitme()   
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        #отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
class Settings():
    """класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """инициализирует настройки игры"""
        #параметры экрана
        self.colors = {'light_green': (0, 255, 255),
                       'blue': (0, 0, 255),
                       'red': (255, 0, 0),
                       'white': (230, 230, 230)}
        self.screen_width = 1200
        self.screen_height = 700
        self.big_color = (230, 230, 230)
        self.ship_speed = 1.5

        #параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

import pygame


class Chest:
    def __init__(self):
        self.items = []
        self.durability = 50
        self.size = 50
        self.is_locked = False
        self.is_opened = False
        self.solid = True

    def open(self):
        if not self.is_opened:
            self.is_opened = True
            self.items = []


class CommonChest(Chest):
    def __init__(self, x, y):
        super().__init__()
        self.x = x * self.size
        self.y = y * self.size
        self.texture = pygame.image.load('images/chest1.bmp')
        self.texture1 = pygame.image.load('images/chest2.bmp')

    def draw(self, screen):
        texture = self.texture
        if self.is_opened:
            texture = self.texture1
        texture = pygame.transform.scale(texture, (self.size, self.size))
        screen.blit(texture, (self.x, self.y))


class ExquisiteChest(Chest):
    def __init__(self):
        super().__init__()
        self.texture = 'yellow'

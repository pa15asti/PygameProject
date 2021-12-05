import random
import pygame


class Ground:
    def __init__(self, x, y):
        self.size = 50
        self.row = x
        self.col = y
        self.x = x * self.size
        self.y = y * self.size
        self.texture = random.choice(['green', 'red', 'yellow'])
        self.durability = 50
        self.solid = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.texture, (self.x, self.y, self.x + self.size, self.y + self.size))

    def destroy(self):
        self.durability = 0
 

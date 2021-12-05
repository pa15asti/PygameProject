import pygame
import ground


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.hp = 100
        self.mp = 100
        self.atk = 10
        self.prt = 10
        self.speed = 10
        self.size = 50
        self.colour = 'blue'
        self.texture = pygame.image.load('images/1.png')
        self.inventory = {'weapons': [], 'armors': [], 'runes': [], 'elemental_crystals': []}

    def draw(self, screen):
        if self.colour:
            pygame.draw.circle(screen, self.colour, (self.x, self.y), 10)

    def x_draw(self, screen):
        texture = self.texture
        texture = pygame.transform.scale(texture, (self.size, self.size))
        screen.blit(texture, (self.x, self.y))

    def change_skin(self, ind):
        pass

    def to_damage(self):
        return self.atk

    def get_damage(self, dmg):
        if self.hp - dmg - self.prt <= 0:
            self.hp = 0
            self.destroy()
        else:
            self.hp -= dmg - self.prt

    def move(self, x, y, items):
        items = [i for i in items if type(i) != ground.Ground]
        if abs(x) > 0.15:
            if not self.is_stuck(x, y, items):
                self.x += int(x * self.speed)
        if abs(y) > 0.15:
            if not self.is_stuck(x, y, items):
                self.y += int(y * self.speed)

    def is_stuck(self, x, y, items):
        new_x = int(self.x + x * self.speed)
        new_y = int(self.y + y * self.speed)
        for i in items:
            if new_x in i.get_pos()[0] and int(self.y) in i.get_pos()[1]:
                return True
            if new_y in i.get_pos()[1] and int(self.x) in i.get_pos()[0]:
                return True
        return False

    def destroy(self):
        print(self)

import pygame


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.hp = 100
        self.mp = 100
        self.atk = 10
        self.prt = 10
        self.speed = 10
        self.colour = "blue"

    def draw(self, screen):
        if self.colour:
            pygame.draw.circle(screen, self.colour, (self.x, self.y), 10)

    def change_colour(self, ind):
        if ind == 2:
            self.colour = "blue"
        if ind == 3:
            self.colour = "yellow"
        if ind == 1:
            self.colour = "red"
        if ind == 0:
            self.colour = "green"

    def to_damage(self):
        return self.atk

    def get_damage(self, dmg):
        if self.hp - dmg - self.prt <= 0:
            self.hp = 0
            self.destroy()
        else:
            self.hp -= dmg - self.prt

    def move(self, x, y):
        if abs(x) > 0.15:
            self.x += x * self.speed
        if abs(y) > 0.15:
            self.y += y * self.speed

    def destroy(self):
        print(self)

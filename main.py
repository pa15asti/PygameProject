import random
import pygame


from player import *
from ground import *
from chest import *
from items import *


class App:
    def __init__(self):
        self.size = 1280, 720
        self.screen = pygame.display.set_mode(self.size)
        self.player = Player()
        self.items = []
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        pygame.display.set_caption("Test")
        self.draw_map()
        self.main()

    def main(self):
        running = True
        fps = 60
        clock = pygame.time.Clock()
        while running:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.JOYBUTTONUP:
                    self.player.change_colour(event.button)
            keys = pygame.key.get_pressed()
            self.input_device(keys)
            self.screen.fill("black")
            [i.draw(self.screen) for i in self.items]
            self.player.draw(self.screen)
            pygame.display.flip()

    def input_device(self, keys=None):
        is_key = False
        if keys:
            if keys[pygame.K_w]:
                self.player.move(0, -1, self.items)
                is_key = True
            if keys[pygame.K_s]:
                self.player.move(0, 1, self.items)
                is_key = True
            if keys[pygame.K_d]:
                self.player.move(1, 0, self.items)
                is_key = True
            if keys[pygame.K_a]:
                self.player.move(-1, 0, self.items)
                is_key = True
            if keys[pygame.K_r]:
                self.draw_map()
            if self.joysticks and not is_key:
                self.player.move(self.joysticks[0].get_axis(0), self.joysticks[0].get_axis(1), self.items)

    def draw_map(self):
        for x in range(self.size[0] // 50):
            for y in range(self.size[1] // 50):
                self.items.append(random.choice([Ground(x, y), Ground(x, y), Ground(x, y), Ground(x, y), Ground(x, y),
                                                 Ground(x, y), Ground(x, y), Ground(x, y), CommonChest(x, y)]))
        for i in self.items:
            i.draw(self.screen)


if __name__ == '__main__':
    pygame.joystick.init()
    pygame.init()
    App()

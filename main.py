import pygame


class App:
    def __init__(self):
        self.size = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.player = Player()
        self.blocks = []
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
            [i.draw(self.screen) for i in self.blocks]
            self.player.draw(self.screen)
            pygame.display.flip()

    def input_device(self, keys=None):
        is_key = False
        if keys:
            if keys[pygame.K_w]:
                self.player.move(0, -1)
                is_key = True
            if keys[pygame.K_s]:
                self.player.move(0, 1)
                is_key = True
            if keys[pygame.K_d]:
                self.player.move(1, 0)
                is_key = True
            if keys[pygame.K_a]:
                self.player.move(-1, 0)
                is_key = True
            if keys[pygame.K_r]:
                self.draw_map()
            if self.joysticks and not is_key:
                self.player.move(self.joysticks[0].get_axis(0), self.joysticks[0].get_axis(1))

    def draw_map(self):
        for x in range(self.size[0] // 50):
            for y in range(self.size[1] // 50):
                self.blocks.append(Ground(x, y))
        for i in self.blocks:
            i.draw(self.screen)


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


class Ground:
    def __init__(self, x, y):
        self.size = 50
        self.x = x * self.size
        self.y = y * self.size
        self.durability = 50

    def draw(self, screen):
        pygame.draw.rect(screen, "green", (self.x, self.y, self.x + self.size, self.y + self.size))

    def destroy(self):
        self.durability = 0


if __name__ == '__main__':
    pygame.joystick.init()
    pygame.init()
    App()

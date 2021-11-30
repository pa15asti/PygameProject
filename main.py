import pygame


class App:
    def __init__(self):
        self.size = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.player = Player()
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        pygame.display.set_caption("Test")
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
            self.screen.fill("black")
            self.player.move(self.joysticks[0])
            self.player.draw(self.screen)
            pygame.display.flip()


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 10
        self.colour = "green"

    def draw(self, screen):
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

    def move(self, joy: pygame.joystick):
        x = joy.get_axis(0)
        y = joy.get_axis(1)
        if abs(x) > 0.15:
            self.x += x * self.speed
        if abs(y) > 0.15:
            self.y += y * self.speed


if __name__ == '__main__':
    pygame.joystick.init()
    pygame.init()
    App()

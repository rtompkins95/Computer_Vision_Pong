import sys, pygame
from config import *


class GameObject:

    def __init__(self, imageFile, speed):
        self.image = pygame.image.load(imageFile)
        self.image_rect = self.image.get_rect()
        self.speed = speed

    def update(self, x, y):
        self.speed = [x, y]

    def move(self):
        return self.image_rect.move(self.speed)


class Game:
    def __init__(self, size):
        self.screen = pygame.display.set_mode(size)
        self.object_list = []
        self.object_list.append(GameObject("ball.gif", [0,0]))
        self.speed = speed
        pygame.init()

    def update(self):
        self.handle_event()

        ballrect = self.object_list[0].move()

        if ballrect.left <= 0:
            ballrect.left = 0
        if ballrect.right >= width:
            ballrect.right = width
        if ballrect.top < 0:
            ballrect.top = 0
        if ballrect.bottom > height:
            ballrect.bottom = height
        self.object_list[0].image_rect = ballrect

    def draw(self):
        self.screen.fill(black)

        for obj in self.object_list:
            self.screen.blit(obj.image, obj.image_rect)
        pygame.display.flip()

    def process_pygame_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

        # increment the ball position by one
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = -vel
            if event.key == pygame.K_RIGHT:
                speed[0] = vel
            if event.key == pygame.K_UP:
                speed[1] = -vel
            if event.key == pygame.K_DOWN:
                speed[1] = vel

        # when the key is released, stop the ball from moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed[0] = 0
            if event.key == pygame.K_RIGHT:
                speed[0] = 0
            if event.key == pygame.K_UP:
                speed[1] = 0
            if event.key == pygame.K_DOWN:
                speed[1] = 0

        for obj in self.object_list:
            obj.update(speed[0], speed[1])

    def handle_event(self):
        for event in pygame.event.get():
            self.process_pygame_event(event)

    def is_playing(self):
        return True


def main():
    game = Game(size)
    while game.is_playing():
        game.update()
        game.draw()

main()

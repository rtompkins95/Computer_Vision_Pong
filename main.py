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
        # self.ball = self.object_list[0].image
        # self.ballrect = self.ball.get_rect()

        # self.paddle_one = self.object_list[1].image
        # self.paddle_one_rect = self.paddle_one.get_rect()

        self.speed = speed
        pygame.init()

    def update(self):
        self.handle_event()

        # generic update
        # for obj in self.object_list:
        #     image_rect = obj.image_rect.move()
        #
        #     if image_rect.left <= 0:
        #         image_rect.left = 0
        #     if image_rect.right >= width:
        #         image_rect.right = width
        #     if image_rect.top < 0:
        #         image_rect.top = 0
        #     if image_rect.bottom > height:
        #         image_rect.bottom = height
        #
        #     obj.image_rect = image_rect

        ballrect = self.object_list[0].move()

        if ballrect.left <= 0:
            ballrect.left = 0
        if ballrect.right >= width:
            ballrect.right = width
        if ballrect.top < 0:
            ballrect.top = 0
        if ballrect.bottom > height:
            ballrect.bottom = height
        #self.ballrect = ballrect
        self.object_list[0].image_rect = ballrect

        # for obj in self.object_list:
        #     obj.update(speed[0], speed[1])
        #     objrect = obj.move()
        #     if objrect.left <= 0:
        #         objrect.left = 0
        #     if objrect.right >= width:
        #         objrect.right = width
        #     if objrect.top < 0:
        #         objrect.top = 0
        #     if objrect.bottom > height:
        #         objrect.bottom = height
        #     self.objrect = ballrect


    def draw(self):
        self.screen.fill(black)

        # one object drawing example
        #self.screen.blit(self.ball, self.ballrect)
        #self.screen.blit(self.paddle_one, self.paddle_one_rect)

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

            #  # player 2 controls
            # if event.key == pygame.K_a:
            #     other_speed[0] = -vel
            # if event.key == pygame.K_d:
            #     other_speed[0] = vel
            # if event.key == pygame.K_w:
            #     other_speed[1] = -vel
            # if event.key == pygame.K_s:
            #     other_speed[1] = vel

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed[0] = 0
            if event.key == pygame.K_RIGHT:
                speed[0] = 0
            if event.key == pygame.K_UP:
                speed[1] = 0
            if event.key == pygame.K_DOWN:
                speed[1] = 0

        # update the ball (object_list[0])
        for obj in self.object_list:
            obj.update(speed[0], speed[1])

        #self.object_list[0].update(speed[0], speed[1])

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

def drawBullet(x, y, bulletSize, gameScreen, vertical=False):
    if vertical:
        pygame.draw.line(gameScreen, green, [x,y], [x, y+bulletSize])
    else:
        pygame.draw.line(gameScreen, green, [x, y], [x+bulletSize, y])

main()

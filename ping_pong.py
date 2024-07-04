from pygame import *
import pygame
from random import randint 


pygame.init()

Back_Color = (randint(0, 255), randint(0, 255), randint(0, 255))

WIDTH = 600
HEIGTH = 500
FPS = 60

window = display.set_mode((WIDTH, HEIGTH))
display.set_caption("PING-PONG")
clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, p_image: str, x: int, y: int, w: int, h: int, speed: int):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed 

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < WIDTH - 80:
            self.rect.x += self.speed

class Ball(GameSprite):
    pass


racket_1 = Player("racket.png", 30, 200, 50, 150, 10)
racket_2 = Player("racket.png", 520, 200, 50, 150, 10)
ball = Ball("tenis_ball.png", 200, 200, 50, 50, 10)

running = True
finish = False

while running:
    for e in event.get():
        if e.type == QUIT:
            running == False

    if not finish:
        window.fill(Back_Color)
        
        racket_1.reset()
        racket_2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
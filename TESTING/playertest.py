import pygame as pg
from pygame.locals import * # needed for K_UP/K_DOWN


class Player(pg.sprite.Sprite):
    def __init__(self, location=(50, 300)):
        super().__init__()
        self.speed = 10
        self.size = 1.2
        displaySize = (round(50 * self.size), round(50 * self.size))
        self.score = 0

        self.surf = pg.surface.Surface(displaySize) # replace w/ scaled image
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(center=location)

    def getSize(self):
        return self.size

    def addSize(self, amount):
        self.size += amount
        self.rect.inflate_ip(amount - 1, amount - 1) # probs change to just amount

    def addScore(self, amount):
        self.score += amount

    def update(self, keypress):
        if keypress[K_UP]:
            self.rect.move_ip(0, -self.speed)

        if keypress[K_DOWN]:
            self.rect.move_ip(0, self.speed)

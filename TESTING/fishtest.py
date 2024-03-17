import pygame as pg
import random as rd


class Fish(pg.sprite.Sprite):
    def __init__(self, location=(500, 500)):
        super().__init__()
        self.speed = rd.randrange(2, 6) # set a random speed for fish to move at
        self.size = rd.uniform(1, 3) # random float size
        displaySize = (round(50 * self.size), round(50 * self.size))
                
        self.surf = pg.surface.Surface(displaySize) # replace w/ image
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect(center=location)

    def getSize(self):
        return self.size

    def getSpeed(self):
        return self.speed

    def addSize(self, amount):
        self.size += amount
        self.rect.inflate_ip(amount - 1, amount - 1) # probs change to just amount
        

    def update(self):
        self.rect.move_ip(-self.speed, 0)

import pygame as pg
import random as rd

class Fish(pg.sprite.Sprite):
    def __init__(self, location=(500, 500)):
        super().__init__()
        self.speed = rd.randrange(2, 6) # set a random speed for fish to move at
        fishSizes = [.5,.5,.6,.75, 1, 1.25, 1.5, 1.75, 2]
        self.size = rd.choice(fishSizes) # random float size
       
        fishList = [
            'game-assets/sprites/fish/bronzegrunt.png',
            'game-assets/sprites/fish/butterfish.png',
            'game-assets/sprites/fish/gulffish.png',
            'game-assets/sprites/fish/herringfish.png',
            'game-assets/sprites/fish/pollockfish.png',
            'game-assets/sprites/fish/sandlacefish.png',
            'game-assets/sprites/fish/sardinefish.png'
        ]
        randImage = rd.choice(fishList)

        self.surf = pg.image.load(randImage)
        self.surf = pg.transform.scale(self.surf, (self.size,self.size))
        self.rect = self.surf.get_rect(center=location)
        
        self.ogImage = self.surf.copy()

    def getSize(self):
        return self.size

    def getSpeed(self):
        return self.speed

    def addSize(self, amount):
        self.size += amount
        self.rect.inflate_ip(amount, amount)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)

        

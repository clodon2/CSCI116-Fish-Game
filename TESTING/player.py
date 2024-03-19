import pygame as pg
from pygame.locals import *

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

class Player(pg.sprite.Sprite):
  def __init__(self, location=(500, 300)):
        super().__init__()
        self.speed = 5
        self.size = 1
        self.score = 0

        self.surf = pg.image.load("game-assets/sprites/player/player1.png") # replace w/ scaled image
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(center=location)
  def getScore(self):
    return self.score

  def addScore(self, amount):
    self.score += amount

  def addSize(self, amount):
    self.size += amount
    self.rect.inflate_ip(amount, amount)

  def getSize(self):
    return self.size

  def getSpeed(self):
    return self.speed

  def update(self, pressedKeys):
    if pressedKeys[K_UP]:
        self.rect.move_ip(-self.speed, 0)
    if pressedKeys[K_DOWN]:
        self.rect.move_ip(self.speed, 0)
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT
  
  

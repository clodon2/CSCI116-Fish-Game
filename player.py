import pygame as pg

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

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
  def getScore(self):
    return self.score

  def addScore(self, amount):
    self.score += amount

  def addSize(self, amount):
    self.size += amount
    self.rect.inflate_ip(amount, amount)

  def update(self, pressedKeys):
    if keypress[K_UP]:
        self.rect.move_ip(-self.speed, 0)
    if keypress[K_DOWN]:
        self.rect.move_ip(self.speed, 0)
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT
  
  

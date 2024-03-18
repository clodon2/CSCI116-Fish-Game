import pygame

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

class Player():
  speed = 5

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
  
  

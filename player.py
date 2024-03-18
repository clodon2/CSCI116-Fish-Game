"""
Program: player.py
Author: Landon Harney
Date-Written: 3/17/2024
Group: Austin Amash, Sam Cremeans, Corey Verkouteren, Landon Harney
Description: This program creates a player for a fish game and allows for movement, score-keeping, and size and speed adjustments.
Variables Used:
SCREEN_HEIGHT - The height of the game screen being displayed
SCREEN_WIDTH - The width of the game screen being displayed
location - The location of where the sprite will be displayed
self.speed - The speed of the fish
self.size - The size of the fish
self.score - The current score in the game
self.surf - The image that is being displayed on the surface
self.rect - The rectangle located around the image
amount - A variable for the score being added
pressedKeys - The keys pressed during the game
"""

# Import the necessary components

import pygame as pg
from pygame.locals import *

# Set Variables

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

class Player(pg.sprite.Sprite):

# Create the player sprite and set parameters
  
  def __init__(self, location=(0, 300)):
        super().__init__()
        self.speed = 5
        self.size = 1
        self.score = 0

        self.surf = pg.image.load(game-assets/sprites/player/player1.png) # replace w/ scaled image
        self.surf = pg.transform.flip(self.surf, True, False)
        self.rect = self.surf.get_rect(center=location)

  # Get the current score and add score over time
    
  def getScore(self):
    return self.score

  def addScore(self, amount):
    self.score += amount

  # Get the size of the fish and add size to player fish

  def addSize(self, amount):
    self.size += amount
    self.rect.inflate_ip(amount, amount)

  def getSize(self):
    return self.size

  # Get the current spped of the player fish

  def getSpeed(self):
    return self.speed

  # Update player movement based on player interactions

  def update(self, pressedKeys):
    if pressedKeys[K_UP]:
        self.rect.move_ip(-self.speed, 0)
    if pressedKeys[K_DOWN]:
        self.rect.move_ip(self.speed, 0)

    # Keep player on the screen
    
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT
  
  

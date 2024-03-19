"""
Program: fish.py
Author: Sam Cremeans
Date-Written: 3/17/2024
Group: Austin Amash, Corey Verkouteren, Landon Harney, Sam Cremeans
Description: This program creates the various fish objects for a fish game via a list and creates random sizes and speeds to provide
    a variety of fish types
Variables Used:
self.speed - Provides the movement speed of the fish object. Randomly assigned value between 2 and 6
fishSizes - List of possible sizes for the fish object. Randomly assigned to fish object.
self.size - Size of the fish object. Gets a random value from fishSizes
fishList - List containing the file paths to fish images. Used to load the graphic for the fish object.
randImage - Stores a randomly selected image path from fishList. Used to load the fish image.
self.surf - Surface associated with the fish object that holds the image loaded from randImage.
self.rect - Rectangle object that specifies the position and size of self.surf. Also used to detect collisions
self.ogImage - Stores a copy of the original image. Used to preserve the original image size and format.
"""



import pygame as pg
import random as rd
#Represents a fish object within the game. Handles appearance, movement, and interaction
class Fish(pg.sprite.Sprite):
    def __init__(self, location=(500, 500)):
        super().__init__()
        self.speed = rd.randrange(2, 6) #Random speed assignment
        fishSizes = [.5,.5,.6,.75, 1, 1.25, 1.5, 1.75, 2]
        self.size = rd.choice(fishSizes) #Random float size
       #Lists paths to fish images
        fishList = [
            'game-assets/sprites/fish/bronzegrunt.png',
            'game-assets/sprites/fish/butterfish.png',
            'game-assets/sprites/fish/gulffish.png',
            'game-assets/sprites/fish/herringfish.png',
            'game-assets/sprites/fish/pollockfish.png',
            'game-assets/sprites/fish/sandlacefish.png',
            'game-assets/sprites/fish/sardinefish.png'
        ]
        #Selects a random image
        randImage = rd.choice(fishList)
        #Loads image
        self.surf = pg.image.load(randImage)
        self.surf = pg.transform.scale(self.surf, (self.size,self.size))
        self.rect = self.surf.get_rect(center=location)
        
        self.ogImage = self.surf.copy()
    #Gets size of fish from self.size
    def getSize(self):
        return self.size
    #Gets speed of fish from self.speed
    def getSpeed(self):
        return self.speed
    #Gets size of fish and adds size to moving fish
    def addSize(self, amount):
        self.size += amount
        self.rect.inflate_ip(amount, amount)
    #Updates fish object in place  
    def update(self):
        self.rect.move_ip(-self.speed, 0)

        

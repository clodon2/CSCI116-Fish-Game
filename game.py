import pygame as pg
from player import Player
from gui import GUI
from fish import Fish
from leaderboard import Leaderboard


class Game:
    def __init__(self, difficulty=1, runTime=120):
        self.screenSize = (800, 600)
        
        self.difficulty = difficulty
        self.pointMultiplier = self.difficulty
        self.runTime = runTime

        self.player = Player()

        self.fishList = []
        self.allSprites = []

    def getFishRects(self):
        return [fish.rect for fish in self.fishList]

    def spawnFish(self):
        return None

    def run(self):
        pg.init()
        screen = pg.display.set_mode(self.screenSize)
        clock = pg.time.Clock()
        running = True

        self.allSprites.append(self.player)

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False


            pressedKeys = pg.key.get_pressed()
            self.player.update(pressedKeys) # move player based on keys pressed

            fishRects = self.getFishRects()
            for fish in self.fishList:
                fish.update() # move fish
                if pg.Rect.colliderect(player.rect, fish.rect):
                    if self.player.getSize() >= fish.getSize():
                        self.player.addSize(fish.getSize())
                    else:
                        self.player.addScore(-5) # player "eaten" here
                        
                hitFish = pg.Rect.collidelistall(fish.rect, fishRects)
                for fishRect in hitFish:
                    otherFish = self.fishList[fishRects.index(fishRect)]
                    # if a fish is behind another and bigger, eat upon collision
                    if fish.rect.left > otherFish.rect.right and \
                       (fish.getSize > otherFish.getSize):
                        fish.addSize(otherFish.getSize())
                        fishRects.remove(fishRect)
                        otherFish.kill()

            screen.fill("blue")

            for entity in self.allSprites:
                entity.blit(entity.surf, entity.rect) # can change if needed

            pg.display.flip()
            clock.tick(60)

        pg.quit()

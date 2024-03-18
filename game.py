"""
Author: Corey Verkouteren
Group: Corey, Austin, Sam, Landon
Description: Main game loop class for the game, combines all parts


"""
import pygame as pg
import random as rd
from player import Player
from gui import GUI
from fish import Fish
from leaderboard import Leaderboard


class Game:
    def __init__(self, difficulty=1, runTime=20):
        self.screenSize = (1000, 600)
        
        self.difficulty = difficulty
        self.pointMultiplier = self.difficulty
        self.runTime = runTime

        self.player = Player()
        self.time = 0 # in seconds of game running

        self.fishList = pg.sprite.Group()
        self.gameSprites = pg.sprite.Group()
        self.GUISprites = []

    def getFishRects(self):
        """Get the rect object of all fish in the fish list and return as a list"""
        return [fish.rect for fish in self.fishList]

    def spawnFish(self):
        """Spawn a fish at a random location within appropriate area"""
        spawnPoint = rd.randrange(10, self.screenSize[1])
        newFish = Fish(location=(self.screenSize[0] + 10, spawnPoint))
        self.fishList.add(newFish)
        self.gameSprites.add(newFish)

    def run(self):
        """run the game"""
        pg.init()
        screen = pg.display.set_mode(self.screenSize)
        clock = pg.time.Clock()
        running = True

        self.gameSprites.add(self.player)

        # put gui stuff in this list
        self.GUISprites = []

        # for fish spawning
        ADDFISH = pg.USEREVENT + 1
        pg.time.set_timer(ADDFISH, 1000)

        # for game end
        GAMEFINISH = pg.USERVENT + 2

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == ADDFISH: # spawn fish event
                    self.spawnFish()

                if event.type == GAMEFINISH: # game ends event
                    print("out of time")
                    self.running = False


            pressedKeys = pg.key.get_pressed()
            self.player.update(pressedKeys) # move player based on keys pressed

            # fish collisions
            self.fishList.update()


            # fish-player collisions
            playerHitFish = pg.sprite.spritecollide(self.player, self.fishList, False)
            for fish in playerHitFish:
                # fish-player collision, if player bigger eat fish
                if self.player.getSize() >= fish.getSize():
                    self.player.addSize(fish.getSize())
                    self.player.addScore(fish.getScore())
                    fish.kill()
                # fish-player collision, if fish bigger "eat" player
                else:
                    self.player.addScore(-5) # player "eaten" here

                # kill fish if swim off screen
                if fish.rect.right < 0:
                    fish.kill()
            
            for fish in self.fishList:
                # fish-fish collisions
                hitFish = pg.sprite.spritecollide(fish, self.fishList, False)
                if hitFish:
                    for otherFish in hitFish:
                        # if a fish is behind another, bigger, and faster, eat
                        # fish in front
                        if fish.rect.left < otherFish.rect.right and \
                           (fish.getSize() > otherFish.getSize()) and \
                           fish.getSpeed() > otherFish.getSpeed():
                            fish.addSize(otherFish.getSize())
                            otherFish.kill()

            if self.time > self.runTime:
                pg.event.post(GAMEFINISH)

            screen.fill("blue")

            # draw all entitites to the screen
            for entity in self.gameSprites:
                screen.blit(entity.surf, entity.rect) # can change if needed

            pg.display.flip()
            clock.tick(60)
            # update time
            self.time += clock.get_time() / 1000

        pg.quit()


myGame = Game()
myGame.run()

"""
Author: Corey Verkouteren
Group: Corey, Austin, Sam, Landon
Description: Main game loop class for the game, combines all parts

Methods:
    spawnFish - Spawn a fish at a random location within appropriate area
    run - runs the game

Variables:
    self.screenSize - size of the window to run the game on
    self.difficulty - intended to affect how fish spawn, etc. NOT IMPLEMENTED
    self.pointMultiplier - connected to difficulty NOT IMPLEMENTED
    self.runTime - time game runs for until game over (seconds)
    self.player - player sprite object
    self.time - time game has been played in seconds
    self.gameFont - font text will be drawn in
    self.fishList - sprite group of "enemy" fish sprites
    self.gameSprites - sprite group of ALL sprites (used for rendering)
    self.UISprites - list of text surface - location tuples (used for rendering)

    spawnPoint - where fish will spawn (within screen size)
    newFish - fish to be spawned

    screen - screen surface we draw everything to
    clock - pygame clock object used for framrate and time keeping
    running - determines if game should continue to run
    hitFish - list of fish that have been collided with
    XXXXText - UI element for a value
"""
import pygame as pg
import random as rd
from player import Player
from fish import Fish
from ScoreBoard import ScoreBoard


class Game:
    def __init__(self, difficulty=1, runTime=60):
        self.screenSize = (1000, 600)
        
        self.difficulty = difficulty # ran out of time
        self.pointMultiplier = self.difficulty # ran out of time
        self.runTime = runTime # time will run for

        self.player = Player()
        self.time = 0 # in seconds of game running
        pg.font.init()
        self.gameFont = pg.font.Font(pg.font.get_default_font(), size=30)

        # sprite groups for updating, collision, and rendering
        self.fishList = pg.sprite.Group()
        self.gameSprites = pg.sprite.Group()
        self.UISprites = []
        

    def spawnFish(self):
        """Spawn a fish at a random location within appropriate area"""
        spawnPoint = rd.randrange(10, self.screenSize[1])
        newFish = Fish(location=(self.screenSize[0] + 10, spawnPoint))
        # add to lists so fish will be updated, etc.
        self.fishList.add(newFish)
        self.gameSprites.add(newFish)

    def run(self):
        """run the game"""
        pg.init()
        screen = pg.display.set_mode(self.screenSize)
        clock = pg.time.Clock()
        running = True

        self.gameSprites.add(self.player)

        # for fish spawning
        ADDFISH = pg.USEREVENT + 1
        pg.time.set_timer(ADDFISH, 1200)

        # for game end
        GAMEFINISH = pg.USEREVENT + 2
        FINISH_EVENT = pg.event.Event(GAMEFINISH)

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == ADDFISH: # spawn fish event
                    self.spawnFish()

                if event.type == GAMEFINISH: # game ends event (time limit)
                    running = False


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
                    self.player.addScore(fish.getSize() * 100)
                    fish.kill()
                # fish-player collision, if fish bigger "eat" player
                else:
                    self.player.addScore(-5) # player "eaten" here
                    self.player.addSize(-5) # lose some size
                    fish.kill() # prevents rapid point loss

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

            # if time is up, run end game command
            if self.time > self.runTime:
                pg.event.post(FINISH_EVENT)

            # text stuff
            self.UISprites = []
            # timer display
            timeText = (self.gameFont.render(f"{round(self.time)}",
                                             True, (255, 255, 255)),
                        (20, 20))
            self.UISprites.append(timeText)

            # score display
            scoreText = (self.gameFont.render(f"{self.player.getScore()}",
                                              True, (255, 255, 255)),
                         (20, 50))
            self.UISprites.append(scoreText)

            # background
            screen.fill("blue")

            # draw all entitites to the screen
            for entity in self.gameSprites:
                screen.blit(entity.surf, entity.rect) # can change if needed

            # draw text over other stuff
            for text in self.UISprites:
                screen.blit(text[0], text[1])

            pg.display.flip()
            clock.tick(60)
            # update time
            self.time += clock.get_time() / 1000

        pg.quit()


# run game
myGame = Game()
myGame.run()

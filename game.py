# Game Item Class with Image
import random
import pygame

class Item:
    def __init__(self,filename,screenSize,speed):
        """Initiate the Item"""
        if filename:
            # read the image from the file
            self.image = pygame.image.load(filename)
            self.rect = self.image.get_rect()
        self.screenSize = screenSize
        self.speed = speed
        # set the initial position
        if filename:
            gap = 10
            self.rect.x = random.randint(gap, self.screenSize[0] - self.rect.width - gap)
            self.rect.y = random.randint(gap, self.screenSize[1] - self.rect.height - gap)

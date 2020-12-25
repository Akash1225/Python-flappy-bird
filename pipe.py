import pygame
import random


class Pipe:
    def __init__(self, scr, gap, width, height):
        self.scr = scr
        self.gap = gap

        self.width = width
        self.height = height

        self.x = self.width
        self.y = random.randrange(0, self.width//2)  # height

        self.pipe_north = pygame.image.load("images/pipeNorth.png")
        self.pipe_south = pygame.image.load("images/pipeSouth.png")

        # set size of pipe
        self.pipe_north = pygame.transform.scale(self.pipe_north, (30, self.y))
        self.pipe_south = pygame.transform.scale(self.pipe_south, (30, self.height-(self.y+self.gap)))

    def update(self):
        self.x -= 5

    def hits(self, bird):
        if (bird.y < self.y or bird.y+bird.r > self.y+self.gap):
            if (bird.x >= self.x and bird.x <= self.x+30):
                return True

    def show(self):
        # TOP PIPE
        # pygame.draw.rect(self.scr, (0, 255, 0),
        #                  pygame.Rect(self.x, 0, 30, self.y))
        self.scr.blit(self.pipe_north, (self.x, 0))

        # BOTTOM PIPE
        # pygame.draw.rect(self.scr, (0, 255, 0), pygame.Rect(
        # self.x, self.y+self.gap, 30, self.height-(self.y+self.gap)))
        self.scr.blit(self.pipe_south, (self.x, self.y+self.gap))

import pygame


class Bird:
    def __init__(self, scr, x, y, r):
        self.x = x
        self.y = y
        self.r = r

        self.vy = 5
        self.lift = -50

        self.scr = scr

        # IMAGES AND SET SIZE
        self.birdImg = pygame.image.load("images/bird.png")
        self.birdImg = pygame.transform.scale(self.birdImg,(self.r,self.r))

    def update(self):
        self.y += self.vy

    def up(self):
        self.y += self.lift

    def show(self):
        # pygame.draw.circle(self.birdImg, (255, 0, 0), (self.x, self.y), self.r)
        self.scr.blit(self.birdImg,(self.x,self.y))

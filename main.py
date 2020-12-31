import pygame
from bird import Bird
from pipe import Pipe
import time

# initiliaze screen
pygame.init()

# GLOBAl variable
WIDTH = 400
HEIGHT = 500
FPS = 30
GAME = True
SCORE = 0

# screen
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird game")
pygame.display.set_icon(pygame.image.load("images/bird.png"))

# clock
clock = pygame.time.Clock()

# IMAGES AND SET SIZE
bgIMG = pygame.image.load("images/bg.png")
bgIMG = pygame.transform.scale(bgIMG, (WIDTH, HEIGHT))

# SOUND
score_sound = pygame.mixer.Sound("sounds/score.mp3")
fly_sound = pygame.mixer.Sound("sounds/fly.mp3")

# msg display function


def msg(text, x, y, color: tuple, size):
    font = pygame.font.SysFont("Times new Roman", size)
    txt = font.render(text, True, color)
    scr.blit(txt, (x, y))


def gameover():
    global GAME
    GAME = False
    scr.fill((0, 0, 0))
    msg(f"Game Over", WIDTH/2-60, HEIGHT/2, (255, 0, 0), 30)
    pygame.display.update()
    time.sleep(5)

# set highscore


def HS(score):
    try:
        with open("highScore.txt", "r") as file:
            high_num = int(file.read())
            if high_num < score:
                with open("highScore.txt", "w") as FileWrite:
                    FileWrite.write(f"{score}")
            return high_num
    except:
        with open("highScore.txt", "w") as FileWrite:
            FileWrite.write(f"{score}")


# game loop
def gameLoop():
    global GAME, WIDTH, HEIGHT, SCORE
    SCORE = 0
    GAME = True

    # bird
    player = Bird(scr, 100, 100, 25)

    # pipe
    pipe = [Pipe(scr, 100, WIDTH, HEIGHT)]

    while GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME = False

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                player.up()
                fly_sound.play()

        # scr.fill((255, 255, 255))
        scr.blit(bgIMG, (0, 0))

        # PLAYER
        player.update()
        player.show()

        # when player hit the ground
        if player.y < 0 or player.y > HEIGHT:
            gameover()

        # pipe
        for i in pipe:
            i.update()
            i.show()

            # add pipe
            if (i.x == 200):
                pipe.append(Pipe(scr, 80, WIDTH, HEIGHT))

            # remove pipe when pipe<0
            if i.x+30<=0:
                pipe.remove(i)

            # add score
            if i.x == player.x:
                SCORE += 1
                score_sound.play()

            # hit the pipe
            if i.hits(player):
                gameover()
                print("HIT")

        print(len(pipe))

        # DIsplay score
        msg(f"{SCORE}", WIDTH/2-60, 0, (0, 0, 0), 30)
        msg(f"{HS(SCORE)}", WIDTH-60, 0, (255, 0, 0), 30)

        # update screen
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    LOOP = True
    while LOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LOOP = False

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                gameLoop()
            elif pressed[pygame.K_q]:
                LOOP = False

        scr.fill((0, 0, 0))
        msg("Space to Play Q for Exit", WIDTH/2-60, HEIGHT/2, (0, 255, 0), 15)
        pygame.display.update()

import pygame
import Classes
import Commands


# 2 important things:

# 1. You will see alot of player.v_v or player.a_q. all of those are explained in the classes file

# 2. if you see something like this:
# "player1.img == player1.imgs[1]"
# It checks the PLAYER's direction
# (player1.imgs[0] = right, player1.imgs[1] = left)

# Setting up the window, refresh rate limit and the players.

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1040
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
REFRESH_RATE = 30

player1 = Classes.Player([pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_e, pygame.K_s, pygame.K_q],
                         400, 605, 100, 100, 0, pygame.image.load('player1.png'))
Commands.cleanpictures(player1.imgs)
player2 = Classes.Player([pygame.K_h, pygame.K_k, pygame.K_u, pygame.K_i, pygame.K_j, pygame.K_y],
                         1400, 605, 100, 100, 1, pygame.image.load('player2.png'))
Commands.cleanpictures(player2.imgs)

# A loop that checks if the players pressed the X button on the top right
# corner of the screen, if he did it closes the game. if not it runs the command rungame.

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    Commands.rungame(screen, player1, player2)
    clock.tick(REFRESH_RATE)

pygame.quit()

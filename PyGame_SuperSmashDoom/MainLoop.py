import pygame
import Classes
import Commands

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1040
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
REFRESH_RATE = 60

player1 = Classes.Player([pygame.image.load('Charecter.R.png').convert(), pygame.image.load('Charecter.L.png').convert()],
                         [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_e, pygame.K_s, pygame.K_q], 400, 600, 100, 100, 0)
Commands.cleanpictures(player1.imgs)
player2 = Classes.Player([pygame.image.load('Charecter.R.png').convert(), pygame.image.load('Charecter.L.png').convert()],
                         [pygame.K_h, pygame.K_k, pygame.K_u, pygame.K_i, pygame.K_j, pygame.K_y], 1400, 600, 100, 100, 1)
Commands.cleanpictures(player2.imgs)

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    Commands.rungame(screen, player1, player2)
    clock.tick(REFRESH_RATE)

pygame.quit()

import pygame
import Classes
import Commands

WINDOW_WIDTH = 920
WINDOW_HEIGHT = 1040
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
REFRESH_RATE = 60

Player1 = Classes.Player([pygame.image.load('Charecter.R.png').convert(),
                          pygame.image.load('Charecter.L.png').convert()],
                         [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_e,
                          pygame.K_s, pygame.K_q], 400, 600, 100, 100, 0)
Commands.cleanpictures(Player1.imgs)
Player2 = Classes.Player([pygame.image.load('Charecter.R.png').convert(),
                          pygame.image.load('Charecter.L.png').convert()],
                         [pygame.K_h, pygame.K_k, pygame.K_u, pygame.K_i,
                          pygame.K_j, pygame.K_y], 1400, 600, 100, 100, 1)
Commands.cleanpictures(Player2.imgs)

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    Commands.Load_BackGround(screen, Player1, Player2)
    keyPressedEvents = pygame.key.get_pressed()
    Commands.keyPressedEvents(keyPressedEvents, Player1)
    Commands.keyPressedEvents(keyPressedEvents, Player2)
    Commands.Gravity(Player1)
    Commands.Gravity(Player2)
    Commands.GroundHitbox(Player1)
    Commands.GroundHitbox(Player2)
    clock.tick(REFRESH_RATE)

pygame.quit()

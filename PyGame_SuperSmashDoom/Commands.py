import pygame
import Classes

second = 22


def rungame(screen, player1, player2):
    won = whowon(player1, player2)
    loadbackground(screen, player1, player2)
    if won is None:
        keypressed = pygame.key.get_pressed()
        keypressedevents(keypressed, player1)
        keypressedevents(keypressed, player2)
        gravity(player1)
        gravity(player2)
        groundhitbox(player1)
        groundhitbox(player2)
        damage(player1, player2)
        damage(player2, player1)
    else:
        pygame.draw.rect(screen, (0, 0, 0), (710, 400, 500, 50))
        font = pygame.font.SysFont(None, 50)
        img = font.render(won, True, (255, 0, 0))
        if won == "Draw":
            screen.blit(img, (1210, 400))
        else:
            screen.blit(img, (910, 400))
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            Classes.Player.restartcharecter(player1, 400, 600)
            Classes.Player.restartcharecter(player2, 1400, 600)
        pygame.display.flip()


def loadbackground(screen, player1, player2):
    screen.blit(pygame.image.load('background.jpg'), (0, 0))

    for i in range(80):
        screen.blit(pygame.image.load('grass_block_side.png'), (16 * i + 320, 700))
        screen.blit(pygame.image.load('dirt.png'), (16 * i + 320, 716))

    screen.blit(player1.img, (player1.x, player1.y))
    screen.blit(player1.icon, (player1.x + 40, player1.y-22))
    screen.blit(player2.img, (player2.x, player2.y))
    screen.blit(player2.icon, (player2.x + 40, player2.y-22))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 210, 30))
    pygame.draw.rect(screen, (255, 0, 0), (5, 5, 200, 20))
    pygame.draw.rect(screen, (0, 225, 0), (5, 5, player1.hp * 2, 20))
    pygame.draw.rect(screen, (0, 0, 0), (1710, 0, 210, 30))
    pygame.draw.rect(screen, (255, 0, 0), (1715, 5, 200, 20))
    pygame.draw.rect(screen, (0, 225, 0), (1715, 5, player2.hp * 2, 20))
    pygame.display.flip()


def keypressedevents(keypressed, player):
    if keypressed[player.b[0]]:
        player.h_v -= 1
        player.img = player.imgs[1]

    if keypressed[player.b[1]]:
        player.h_v += 1
        player.img = player.imgs[0]

    if keypressed[player.b[0]] == 0 and keypressed[player.b[1]] == 0 and player.h_v != 0:
        player.h_v = reducetozero(player.h_v)

    player.h_v = maxmin(player.h_v, -15, 15)

    if keypressed[player.b[2]] and player.canjump == True:
        player.jump = True
        player.canjump = False

    if keypressed[player.b[3]] and player.e == True and player.a_s == False and player.a_q == False:
        player.a_e = True
        player.e = False
        player.v_v = 0

    if keypressed[pygame.K_t]:
        player.hp = 0

    if keypressed[player.b[4]] and player.s == True and player.a_e == False and player.a_q == False:
        player.s_charge += 1
        if player.s_charge == 15:
            player.s_charge = 0
            player.a_s = True
            player.s = False
    else:
        player.s_charge = 0

    if player.a_s:
        if player.img == player.imgs[1] and player.s_v == 0:
            player.s_v = -1
        if player.img == player.imgs[0] and player.s_v == 0:
            player.s_v = 1

        if player.a_h_v == 0:
            player.a_h_v = 81 * player.s_v
        elif player.a_h_v == player.s_v:
            player.a_h_v = 0
            player.a_s = False
            player.s_d = True
            player.s_v = 0
        else:
            player.a_h_v -= 5 * player.s_v

    else:
        if not player.s:
            player.s_c += 1
        if player.s_c == 10 * second:
            player.s_c = 0
            player.s = True

    if keypressed[player.b[5]] and player.q == True and player.a_e == False and player.a_s == False:
        player.a_q = True
        player.q = False
        player.v_v = 0

    if player.a_q:
        if player.a_v_v == 0:
            player.a_v_v = -16
        elif player.a_v_v == -1:
            player.a_v_v = 1
        elif 16 > player.a_v_v > 0:
            player.a_v_v = player.a_v_v * 2
        elif player.a_v_v == 16:
            if player.y == 700 - player.h and 320 - player.w <= player.x <= 1600:
                player.a_v_v = 0
                player.a_q = False
                player.q_d = True
        else:
            player.a_v_v = player.a_v_v / 2
        if player.a_v_v != 0:
            if player.img == player.imgs[0]:
                player.a_h_v = 16
            else:
                player.a_h_v = -16
        else:
            player.a_h_v = 0
    elif not player.q:
        if player.q_c <= 10 * second:
            player.q_c += 1
        else:
            player.q = True
            player.q_c = 0

    player.x = player.x + player.h_v + player.a_h_v + player.e_h_v
    player.e_h_v = reducetozero(player.e_h_v)


def maxmin(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n


def reducetozero(n):
    if n > 0:
        return n - 1
    elif n < 0:
        return n + 1
    else:
        return n


def roundnum(numtoround, num):
    if num - 5 <= numtoround <= num + 15:
        return num
    else:
        return numtoround


def groundhitbox(player):
    if 732 > player.y > 700 - player.h and 320 - player.w <= player.x <= 1600:
        if 320 - player.w < player.x <= 320 - player.w + player.h_v + player.a_h_v + player.e_h_v or \
                1600 - player.h_v - player.a_h_v - player.e_h_v <= player.x < 1600:
            player.x -= player.h_v

        if 732 > player.y > 700 - player.h:
            if 320 <= player.x + player.h_v <= 360:
                player.x -= player.h_v

        player.y = roundnum(player.y, 600)
        if player.y == roundnum(player.y, 600) and 320 - player.w <= player.x <= 1600:
            player.v_v = 0
        player.y = roundnum(player.y, 660)


def gravity(player):
    if player.y == 700 - player.h and 320 - player.w <= player.x <= 1600:
        player.v_v = 0
        player.canjump = True
    elif player.jump == False and player.a_e == False and player.a_q == False:
        player.v_v += 1
    maxmin(player.v_v, -15, 15)

    if player.jump:
        if player.v_v >= 0:
            player.v_v = -32
        elif player.v_v == -1:
            player.v_v = 0
            player.jump = False
        else:
            player.v_v = player.v_v / 2

    if player.a_e:
        if player.a_v_v >= 0:
            player.a_v_v = -64
        elif player.a_v_v == -1:
            player.a_v_v = 0
            player.a_e = False
        else:
            player.a_v_v = player.a_v_v / 2
    else:
        player.e_c += 1
        if player.e_c == 10 * second:
            player.e = True
            player.e_c = 0
            player.e_d = True

    player.v_v = maxmin(player.v_v, -100, 15)
    player.y = player.y + player.v_v + player.a_v_v + player.e_v_v
    player.e_v_v = reducetozero(player.e_v_v)


def cleanpictures(imgs):
    white = (255, 255, 255)
    for i in range(len(imgs)):
        imgs[i].set_colorkey(white)


def damage(player1, player2):
    if player1.a_e and player1.y - 100 <= player2.y <= player1.y + player1.h:
        if (player1.img == player1.imgs[1] and player1.x - 100 - player1.w <= player2.x <= player1.x) \
                or (player1.img == player1.imgs[0] and player1.x <= player2.x <= player1.x + 100 + player1.w):
            if player1.e_d:
                player1.e_d = False
                player2.hp -= 5
                player2.e_v_v -= 20

    if player1.q_d:
        if (player1.img == player1.imgs[1] and player1.x - 100 - player1.w <= player2.x <= player1.x + player1.w) or \
                (player1.img == player1.imgs[0] and player1.x <= player2.x <= player1.x + 100 + player1.w):
            player2.hp -= 5
            player1.q_d = False
            player2.e_v_v -= 10
            if player1.img == player1.imgs[1]:
                player2.e_h_v -= 20*player2.kb
            else:
                player2.e_h_v += 20*player2.kb
        else:
            player1.q_d = False

    if player1.a_s and player1.y - 100 <= player2.y <= player1.y + player1.h:
        if (player1.img == player1.imgs[1] and player1.x - 50 - player1.w <= player2.x <= player1.x) or \
                (player1.img == player1.imgs[0] and player1.x <= player2.x <= player1.x + 50 + player1.w):
            if player1.s_d:
                player1.s_d = False
                player1.a_h_v = 0
                player1.a_s = False
                player2.hp -= 5
                if player1.img == player1.imgs[1]:
                    player2.e_h_v -= 20*player2.kb
                else:
                    player2.e_h_v += 20*player2.kb

    if player1.x > 1920 or player1.x + player1.w < 0 or player1.y < -player1.h or player1.y > 1040:
        if player1.o <= 10:
            player1.hp -= 1
            player1.o += 1
        else:
            Classes.Player.restartabillities(player1)
            player1.x, player1.y, player1.o = 870, 500, 0
    player2.kb = maxmin((100 - player2.hp)/20, 1, 1.7)


def whowon(player1, player2):
    if player1.hp <= 0:
        if player2.hp <= 0:
            return "Draw"
        else:
            return "Player 2 Won"
    elif player2.hp <= 0:
        return "Player 1 Won"
    else:
        return None

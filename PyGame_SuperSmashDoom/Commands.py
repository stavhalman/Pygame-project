import pygame


def loadbackground(screen, player_1, player_2):
    screen.blit(pygame.image.load('background.jpg'), (0, 0))

    for i in range(80):
        screen.blit(pygame.image.load('grass_block_side.png'), (16 * i + 320, 700))
        screen.blit(pygame.image.load('dirt.png'), (16 * i + 320, 716))

    screen.blit(player_1.img, (player_1.x, player_1.y))
    screen.blit(player_2.img, (player_2.x, player_2.y))

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
        player.x, player.y = 700, 400

    if keypressed[player.b[4]] and player.s == True and player.a_e == False and player.a_q == False:
        player.s_charge += 1
        if player.s_charge == 15:
            player.s_charge = 0
            player.a_s = True
            player.s = False
    else:
        player.q_charge = 0

    if player.a_s:
        if player.img == player.imgs[1] and player.s_d == 0:
            player.s_d = -1
        if player.img == player.imgs[0] and player.s_d == 0:
            player.s_d = 1

        if player.a_h_v == 0:
            player.a_h_v = 61 * player.s_d
        elif player.a_h_v == player.s_d:
            player.a_h_v = 0
            player.a_s = False
            player.s_d = 0
        else:
            player.a_h_v -= 5 * player.s_d

    else:
        if not player.s:
            player.s_c += 1
        if player.s_c == 20:
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
        else:
            player.a_v_v = player.a_v_v / 2
        if player.a_v_v != 0:
            if player.img == player.imgs[0]:
                player.a_h_v = 16
            else:
                player.a_h_v = -16
        else:
            player.a_h_v = 0
            player.q = True

    player.x = player.x + player.h_v + player.a_h_v


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
    if n < 0:
        return n + 1


def roundnum(numtoround, num):
    if num - 5 <= numtoround <= num + 15:
        return num
    else:
        return numtoround


def groundhitbox(player):
    if 732 > player.y > 700 - player.h and 320 - player.w <= player.x <= 1600:
        if 320 - player.w < player.x <= 320 - player.w + player.h_v or 1600 - player.h_v <= player.x < 1600:
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

    if not player.e:
        player.e_c += 1
        if player.e_c == 30:
            player.e = True
            player.e_c = 0

    player.v_v = maxmin(player.v_v, -100, 15)
    player.y = player.y + player.v_v + player.a_v_v


def cleanpictures(imgs):
    white = (255, 255, 255)
    for i in range(len(imgs)):
        imgs[i].set_colorkey(white)

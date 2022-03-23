import pygame
import Classes

def Load_BackGround(screen,Player_1,Player_2):
    screen.blit(pygame.image.load('background.jpg'), (0, 0))

    for i in range(80):
        screen.blit(pygame.image.load('grass_block_side.png'), (16*i+320, 700))
        screen.blit(pygame.image.load('dirt.png'), (16 * i + 320, 716))

    screen.blit(Player_1.img, (Player_1.x, Player_1.y))
    screen.blit(Player_2.img, (Player_2.x, Player_2.y))

    pygame.display.flip()

def keyPressedEvents(keyPressedEvents,Player):

    if keyPressedEvents[Player.b[0]]:
        Player.h_v -= 1
        Player.img = Player.imgs[1]

    if keyPressedEvents[Player.b[1]]:
        Player.h_v += 1
        Player.img = Player.imgs[0]

    if keyPressedEvents[Player.b[0]] == 0 and keyPressedEvents[Player.b[1]] == 0 and Player.h_v != 0:
        Player.h_v = ReduceToZero(Player.h_v)

    Player.h_v = MaxMin(Player.h_v,-15,15)

    if keyPressedEvents[Player.b[2]] and Player.canjump == True:
        Player.jump = True
        Player.canjump = False

    if keyPressedEvents[Player.b[3]] and Player.e == True:
        Player.a_e = True
        Player.e = False
        Player.v_v = 0

    if keyPressedEvents[pygame.K_t]:
        Player.x,Player.y = 700,400

    if keyPressedEvents[Player.b[4]] and Player.q == True:
        Player.q_charge +=1
        if Player.q_charge == 15:
            Player.q_charge = 0
            Player.a_q = True
            Player.q = False
    else:
        Player.q_charge = 0

    if Player.a_q == True:
        if Player.img == Player.imgs[1] and Player.q_d == 0:
            Player.q_d = -1
        if Player.img == Player.imgs[0] and Player.q_d == 0:
            Player.q_d = 1

        if Player.a_h_v == 0:
            Player.a_h_v = 61*Player.q_d
        elif Player.a_h_v == Player.q_d:
            Player.a_h_v = 0
            Player.a_q = False
            Player.q_d = 0
        else:
            Player.a_h_v -= 5*Player.q_d

    else:
        if Player.q == False:
            Player.q_c +=1
        if Player.q_c == 20:
            Player.q_c = 0
            Player.q = True

    Player.x = Player.x + Player.h_v + Player.a_h_v


def MaxMin(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

def ReduceToZero(n):
    if n > 0:
        return n-1
    if n < 0:
        return n+1

def RoundNum(numtoround,num):
    if num-5 <= numtoround <= num+15:
        return num
    else:
        return numtoround

def GroundHitbox(Player):
    if 732 > Player.y > 700-Player.h and 320-Player.w <= Player.x <= 1600:
        if 320-Player.w < Player.x <= 320-Player.w+Player.h_v or 1600-Player.h_v <= Player.x < 1600:
            Player.x -= Player.h_v

        if 732 > Player.y > 700-Player.h:
            if 320 <= Player.x+Player.h_v <= 360:
                Player.x -= Player.h_v

        Player.y = RoundNum(Player.y,600)
        if Player.y == RoundNum(Player.y,600) and 320-Player.w <= Player.x <= 1600:
            Player.v_v = 0
        Player.y = RoundNum(Player.y,660)

def Gravity(Player):
    if Player.y == 700-Player.h and 320-Player.w <= Player.x <= 1600:
        Player.v_v = 0
        Player.a_v_v = 0
        Player.canjump = True
    elif Player.jump == False and Player.a_e == False:
        Player.v_v += 1
    MaxMin(Player.v_v, -15, 15)

    if Player.jump == True:
        if Player.v_v >= 0:
            Player.v_v = -32
        elif Player.v_v == -1:
            Player.v_v = 0
            Player.jump = False
        else:
            Player.v_v = Player.v_v/2

    if Player.a_e == True:
        if Player.a_v_v >= 0:
            Player.a_v_v = -64
        elif Player.a_v_v == -1:
            Player.a_v_v = 0
            Player.a_e = False
        else:
            Player.a_v_v = Player.a_v_v/2

    if Player.e == False:
        Player.e_c += 1
        if Player.e_c == 30:
            Player.e = True
            Player.e_c = 0

    Player.v_v = MaxMin(Player.v_v,-100,15)
    Player.y = Player.y + Player.v_v + Player.a_v_v

def cleanpictures(imgs):
    WHITE = (255, 255, 255)
    for i in range(len(imgs)):
        imgs[i].set_colorkey(WHITE)




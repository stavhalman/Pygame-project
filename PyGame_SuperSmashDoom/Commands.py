import pygame
import Classes

# An integer which I found that if multiplied by a number it makes him to be in seconds
# ( 5*second = five seconds)
second = 24


# A program which rounds the integer if the number and
# the second argument close to each other by 10.
def roundnum(numtoround, num):
    if num - 10 <= numtoround <= num + 10:
        return num
    else:
        return numtoround


# A program which limits an integer to be between the two arguments min and max.
def maxmin(n, min, max):
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n


# A program which lower/raise the integer by 1 until it reaches 0.
def reducetozero(n):
    if n > 0:
        return n - 1
    elif n < 0:
        return n + 1
    else:
        return n


# A program which checks if any PLAYER has won, or if there is a draw
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


# A program which take s all the pictures that are being used to draw the player and removes the background
def cleanpictures(imgs):
    white = (255, 255, 255)
    for i in range(len(imgs)):
        imgs[i].set_colorkey(white)


# A program which runs all the main programs unless a PLAYER won,
# if a PLAYER won it stops the game and write the winner at the center of
# the screen until the space bar is pressed.
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
        font = pygame.font.SysFont(None, 100)
        img = font.render(won, True, (255, 0, 0))
        if won == "Draw":
            screen.blit(img, (850, 400))
        else:
            screen.blit(img, (710, 400))
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            Classes.Player.restartcharecter(player1, 400, 600)
            Classes.Player.restartcharecter(player2, 1400, 600)
        pygame.display.flip()


# A program which draws the background, PLAYERS and their HP bars.
def loadbackground(screen, player1, player2):
    screen.blit(pygame.image.load('background.jpg'), (0, 0))

    for i in range(80):
        screen.blit(pygame.image.load('grass_block_side.png'), (16 * i + 320, 700))
        screen.blit(pygame.image.load('dirt.png'), (16 * i + 320, 716))

    screen.blit(player1.img, (player1.x, player1.y))
    screen.blit(player1.icon, (player1.x + 40, player1.y - 22))
    screen.blit(player2.img, (player2.x, player2.y))
    screen.blit(player2.icon, (player2.x + 40, player2.y - 22))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 210, 30))
    pygame.draw.rect(screen, (255, 0, 0), (5, 5, 200, 20))
    pygame.draw.rect(screen, (0, 225, 0), (5, 5, player1.hp * 2, 20))
    pygame.draw.rect(screen, (0, 0, 0), (1710, 0, 210, 30))
    pygame.draw.rect(screen, (255, 0, 0), (1715, 5, 200, 20))
    pygame.draw.rect(screen, (0, 225, 0), (1715, 5, player2.hp * 2, 20))
    pygame.display.flip()


# Each PLAYER has a list of keys, the program check if the PLAYER's keys are being pressed.
def keypressedevents(keypressed, player):
    # Movement to the left.
    if keypressed[player.b[0]]:
        player.h_v -= 1
        player.img = player.imgs[1]
    # Movement to the right.
    if keypressed[player.b[1]]:
        player.h_v += 1
        player.img = player.imgs[0]
    # If the PLAYER isn't trying to move it slows him down until he isn't moving.
    if keypressed[player.b[0]] == 0 and keypressed[player.b[1]] == 0 and player.h_v != 0:
        player.h_v = reducetozero(player.h_v)
    # Limit the player's normal horizontal movement.
    player.h_v = maxmin(player.h_v, -15, 15)

    # The "Jump" ability
    if keypressed[player.b[2]] and player.canjump == True:
        player.jump = True
        player.canjump = False

    # "E" ability, while checking no other ability is activated.
    if keypressed[player.b[3]] and player.e == True and player.a_s == False and player.a_q == False:
        player.a_e = True
        player.e = False
        player.v_v = 0

    # "S" ability, while checking no other ability is activated.
    # The PLAYER needs to charge the ability to activate it.
    if keypressed[player.b[4]] and player.s == True and player.a_e == False and player.a_q == False:
        player.s_charge += 1
        if player.img == player.imgs[1] or player.img == player.imgs[3]:
            player.img = player.imgs[3]
        elif player.img == player.imgs[0] or player.img == player.imgs[2]:
            player.img = player.imgs[2]

        if player.s_charge == 15:
            player.s_charge = 0
            player.a_s = True
            player.s = False
            player.s_d = False
    else:
        player.s_charge = 0
        if player.img == player.imgs[3]:
            player.img = player.imgs[1]
        elif player.img == player.imgs[2]:
            player.img = player.imgs[0]

    # This is the "S" ability which lunches the PLAYER forward
    if player.a_s:
        if (player.img == player.imgs[1] or player.img == player.imgs[3]) and player.s_v == 0:
            player.s_v = -1
        if (player.img == player.imgs[0] or player.img == player.imgs[2]) and player.s_v == 0:
            player.s_v = 1

        if player.a_h_v == 0:
            player.a_h_v = 81 * player.s_v
        elif player.a_h_v == player.s_v:
            player.a_h_v = 0
            player.a_s = False
            player.s_v = 0
        else:
            player.a_h_v -= 5 * player.s_v

    else:
        if not player.s:
            player.s_c += 1
        if player.s_c == 5 * second:
            player.s_c = 0
            player.s = True

    # "Q" ability, while checking no other ability is activated.
    if keypressed[player.b[5]] and player.q == True and player.a_e == False and player.a_s == False:
        player.a_q = True
        player.q = False
        player.v_v = 0

    # This is the "Q" ability which throws the PLAYER forward,
    # (the Player can change the direction of the ability midair).
    if player.a_q:
        if player.a_v_v == 0:
            player.a_v_v = -16
        elif player.a_v_v == -1:
            player.a_v_v = 1
        elif 16 > player.a_v_v > 0:
            player.a_v_v = player.a_v_v * 2
        elif player.a_v_v == 16:
            if roundnum(player.y, 600) == 700 - player.h and 320 - player.w <= player.x <= 1600:
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
        if player.q_c <= 5 * second:
            player.q_c += 1
        else:
            player.q = True
            player.q_c = 0

    player.x = player.x + player.h_v + player.a_h_v + player.e_h_v
    player.e_h_v = reducetozero(player.e_h_v)


# A program which make sure that if the player doesn't stand on the ground/uses any ability he falls.
# Also, if PLAYER1 is out of the map it deals him damage and then teleports him back to the platform
def gravity(player):
    # If the PLAYER stands on the ground.
    if 320 - player.w <= player.x <= 1600:
        player.y = roundnum(player.y, 600)
    if player.y == 700 - player.h and 320 - player.w <= player.x <= 1600:
        player.v_v, player.e_v_v = 0, 0
        player.canjump = True
    # If the PLAYER isn't jumping/using any ability.
    elif player.jump == False and player.a_e == False and player.a_q == False:
        player.v_v += 1
    maxmin(player.v_v, -15, 15)

    # This is the "JUMP" ability which lunches the PLAYER upwards.
    if player.jump:
        if player.v_v >= 0:
            player.v_v = -64
        elif player.v_v == -1:
            player.v_v = 0
            player.jump = False
        else:
            player.v_v = player.v_v / 2

    # This is the "E" ability which greatly lunches the PLAYER upwards,
    # if there is an enemy in the way it deals him damage.
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
        if player.e_c == 5 * second:
            player.e = True
            player.e_c = 0
            player.e_d = True

    # Limits the Vertical Velocity of the PLAYER and changes the Y position of the PLAYER accordingly.
    # Also, it reduces the Enemy vertical Velocity by 1
    player.v_v = maxmin(player.v_v, -100, 15)
    player.y = player.y + player.v_v + player.a_v_v + player.e_v_v
    player.e_v_v = reducetozero(player.e_v_v)


# A program which make sure that the PLAYER can enter the ground.
def groundhitbox(player):
    if 320 - player.w <= player.x + player.h_v + player.a_h_v + player.e_h_v <= 1600 and \
            700 - player.h < player.y + player.v_v + player.a_v_v + player.e_v_v <= 720:

        if 320 - player.w <= player.x + player.h_v + player.a_h_v + player.e_h_v <= 1600:
            player.x -= player.h_v + player.a_h_v + player.e_h_v


# A program the checks if PLAYER1 uses an ability, and if PLAYER2 is in the ability hit-box when
# the ability do the damage it lowers PLAYER2 HP and knocks him back. There is a knock-back multiplayer which
# makes the PLAYER take more knock-back as his HP gets lower
def damage(player1, player2):
    # "E" ability
    if player1.a_e and player1.y - 100 <= player2.y <= player1.y + player1.h:
        if (player1.img == player1.imgs[1] and player1.x - 100 - player1.w <= player2.x <= player1.x) \
                or (player1.img == player1.imgs[0] and player1.x <= player2.x <= player1.x + 100 + player1.w):
            if player1.e_d:
                player1.e_d = False
                player2.hp -= 2
                player2.e_v_v -= 20
    # "Q" ability
    if player1.q_d:
        if (player1.img == player1.imgs[1] and player1.x - 100 - player1.w <= player2.x <= player1.x + 50 + player1.w) or \
                (player1.img == player1.imgs[0] and player1.x - 50 <= player2.x <= player1.x + 100 + player1.w):
            player2.hp -= 3
            player1.q_d = False
            player2.e_v_v -= 10
            if player1.img == player1.imgs[1]:
                player2.e_h_v -= 20 * player2.kb
            else:
                player2.e_h_v += 20 * player2.kb
        else:
            player1.q_d = False

    # "S" ability
    if player1.a_s and player1.y - 100 <= player2.y <= player1.y + player1.h:
        if (player1.img == player1.imgs[1] and player1.x - 50 - player1.w <= player2.x <= player1.x) or \
                (player1.img == player1.imgs[0] and player1.x <= player2.x <= player1.x + 50 + player1.w):
            if not player1.s_d:
                player1.s_d = True
                player1.a_h_v = 0
                player1.a_s = False
                player2.hp -= 5
                if player1.img == player1.imgs[1]:
                    player2.e_h_v -= 20 * player2.kb
                else:
                    player2.e_h_v += 20 * player2.kb

    # If PLAYER1 is out of the map, it makes him take damage and then
    # teleports him the in middle of the platform
    if player1.x > 1920 or player1.x + player1.w < 0 or player1.y < -player1.h or player1.y > 1040:
        if player1.o <= 10:
            player1.hp -= 1
            player1.o += 1
        else:
            Classes.Player.restartabillities(player1)
            player1.x, player1.y, player1.o = 870, 500, 0
    player2.kb = maxmin((100 - player2.hp) / 20, 1, 1.7)

import pygame


class Entity:
    def __init__(self, xposition, yposition, width, hight, img):
        self.x = xposition
        self.y = yposition
        self.w = width
        self.h = hight
        self.img = img


class Player:
    def __init__(self, buttons, xposition, yposition, width, hight, img, icon):
        self.imgs = [pygame.image.load('Charecter.R.png').convert(),
                     pygame.image.load('Charecter.L.png').convert(),
                     pygame.image.load('Charecter.R.S.png').convert(),
                     pygame.image.load('Charecter.L.S.png').convert()]  # A lists of images of the PLAYER
        self.b = buttons  # A lists of keys of the PLAYER
        self.x = xposition
        self.y = yposition
        self.w = width
        self.h = hight
        self.startimage = img  # A integer that helps choose he correct picture after a restart
        self.img = self.imgs[img]  # A starting image of the PLAYER
        self.icon = icon  # A picture of the icon that is on top of the PLAYER

        self.v_v = 0  # The PLAYER's Vertical Velocity
        self.h_v = 0  # The PLAYER's Horizontal Velocity
        self.a_v_v = 0  # The PLAYER's Ability Vertical Velocity
        self.a_h_v = 0  # The PLAYER's Horizontal Vertical Velocity
        self.e_v_v = 0  # The PLAYER's Vertical Velocity that the Enemy inflicted on the PLAYER
        self.e_h_v = 0  # The PLAYER's Horizontal Velocity that the Enemy inflicted on the PLAYER

        self.jump = False  # Is the PLAYER jumping?
        self.canjump = True  # Can the PLAYER jump?

        self.e = True  # Is the "E" ability available?
        self.a_e = False  # Is the "E" ability Activated?
        self.e_c = 0  # The "E" ability Cooldown timer
        self.e_d = True  # Did the "E" ability already made the Damage to the other PLAYER?

        self.s = True  # Is the "S" ability available?
        self.a_s = False  # Is the "S" ability Activated?
        self.s_c = 0  # The "S" ability Cooldown timer
        self.s_charge = 0  # How much the PLAYER has charged the ability
        self.s_v = 0  # The "S" ability direction (the V stand for velocity since s_d is for Damage)
        self.s_d = True  # Did the "S" ability already made the Damage to the other PLAYER?

        self.q = True  # Is the "Q" ability available?
        self.a_q = False  # Is the "Q" ability Activated?
        self.q_c = 0  # The "Q" ability Cooldown timer
        self.q_d = False  # Did the "Q" ability already made the Damage to the other PLAYER?

        self.hp = 100  # The PLAYER's Health Points
        self.o = 0  # How many frames has the PLAYER been Out of the map
        self.kb = 0  # Knock-Back multiplayer

    # A programs that reset all the PLAYER's stats
    def restartcharecter(self, x, y):
        self.v_v = 0
        self.h_v = 0
        self.a_v_v = 0
        self.a_h_v = 0
        self.e_v_v = 0
        self.e_h_v = 0
        self.jump = 0
        self.canjump = True
        self.e = True
        self.a_e = False
        self.e_c = 0
        self.e_d = True
        self.s = True
        self.a_s = False
        self.s_c = 0
        self.s_charge = 0
        self.s_v = 0
        self.s_d = True
        self.q = True
        self.a_q = False
        self.q_c = 0
        self.q_d = False
        self.hp = 100
        self.o = 0
        self.x = x
        self.y = y
        self.img = self.imgs[self.startimage]

    # A program that reset the PLAYER's abilities and velocities
    def restartabillities(self):
        self.canjump = True
        self.a_e = False
        self.e_d = True
        self.a_s = False
        self.s_charge = 0
        self.s_v = 0
        self.s_d = True
        self.a_q = False
        self.q_d = False
        self.o = 0
        self.v_v = 0
        self.h_v = 0
        self.e_v_v = 0
        self.e_h_v = 0
        self.a_v_v = 0
        self.a_h_v = 0

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
        self.imgs = [pygame.image.load('Charecter.R.png').convert(), pygame.image.load('Charecter.L.png').convert()]
        self.b = buttons
        self.x = xposition
        self.y = yposition
        self.w = width
        self.h = hight
        self.img = self.imgs[img]
        self.icon = icon
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
        self.e_d = True
        self.q = True
        self.a_q = False
        self.q_c = 0
        self.q_d = False
        self.hp = 100
        self.o = 0

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

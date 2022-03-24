class Entity:
    def __init__(self, xposition, yposition, width, hight, img):
        self.x = xposition
        self.y = yposition
        self.w = width
        self.h = hight
        self.img =img



class Player:
    def __init__(self,images,buttons,xposition,yposition,width,hight,img):
        self.imgs = images
        self.b = buttons
        self.x = xposition
        self.y = yposition
        self.w = width
        self.h = hight
        self.img = self.imgs[img]
        self.v_v = 0
        self.h_v = 0
        self.a_v_v = 0
        self.a_h_v = 0
        self.jump = 0
        self.canjump = True
        self.e = True
        self.a_e = False
        self.e_c = 0
        self.s = True
        self.a_s = False
        self.s_c = 0
        self.s_charge = 0
        self.s_d = 0
        self.q = True
        self.a_q = False
        self.q_c = 0
        self.hp = 100


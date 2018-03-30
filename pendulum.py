import pygame
import sys
import math


class Pendulum(object):
    def __init__(self):
        pygame.init()
        self.SCREEN_SIZE = (800,800)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        #self.screen2 = pygame.display.set_mode(self.SCREEN_SIZE)

        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.tps_max = 300.0

        self.r1 = 200
        self.r2 = 200
        self.m1 = 40
        self.m2 = 20

        self.x2tab = []
        self.y2tab = []

        self.px2tab = []
        self.py2tab = []

        self.x0 = 400
        self.y0 = 200

        self.x1 = 0
        self.y1 = 0

        self.x2 = 0
        self.y2 = 0

        self.teta1 = math.pi/2
        self.teta2 = math.pi/2

        self.teta1_v = 0
        self.teta2_v = 0

        self.teta1_a = 0
        self.teta2_a = 0

        self.px2 = -1
        self.py2 = -1

        self.x2tab.append(self.x2)
        self.y2tab.append(self.y2)

        self.px2tab.append(self.px2)
        self.py2tab.append(self.py2)

        self.c = 0


        self.g = 0.02




        while True:

            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1/ self.tps_max

            self.screen.fill((0,0,0))
            self.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def tick(self):

        self.x1 = self.x0 + self.r1 * math.sin(self.teta1)
        self.y1 = self.y0 + self.r1 * math.cos(self.teta1)
        #print(self.teta1)
        self.x2 = self.x1 + self.r2 * math.sin(self.teta2)
        self.y2 = self.y1 + self.r2 * math.cos(self.teta2)

        self.teta1_a = (-self.g*(2*self.m1 + self.m2)*math.sin(self.teta1) - self.m2*self.g*math.sin(self.teta1-2*self.teta2) - 2*math.sin(self.teta1 - self.teta2)*self.m2*(self.teta2_v*self.teta2_v*self.r2 + self.teta1_v * self.teta1_v * self.r1*math.cos(self.teta1-self.teta2)))/(self.r1*(2*self.m1+self.m2 - self.m2*math.cos(2*self.teta1-2*self.teta2)))

        self.teta2_a =(2*math.sin(self.teta1-self.teta2)*(self.teta1_v*self.teta1_v*self.r1*(self.m1+self.m2)+self.g*(self.m1+self.m2)*math.cos(self.teta1)+self.teta2_v*self.teta2_v*self.r2*self.m2*math.cos(self.teta1-self.teta2)))/(self.r2*(2*self.m1+self.m2-self.m2*math.cos(2*self.teta1-2*self.teta2)))

        self.teta1_v += self.teta1_a
        self.teta2_v += self.teta2_a

        self.teta1_v *= 0.99999
        self.teta2_v *= 0.99999

        self.teta1 += self.teta1_v
        self.teta2 += self.teta2_v

        self.px2 = self.x2
        self.py2 = self.y2

        self.x2tab.append(self.x2)
        self.y2tab.append(self.y2)

        self.px2tab.append(self.px2)
        self.py2tab.append(self.py2)


    def draw(self):




        pygame.draw.line(self.screen,(255,255,255),(self.x0,self.y0),(self.x1,self.y1),1)
        pygame.draw.ellipse(self.screen,(255,255,255),(self.x1 - self.m1/2, self.y1 - self.m1/2, self.m1, self.m1))

        pygame.draw.line(self.screen,(255,255,255),(self.x1,self.y1), (self.x2, self.y2), 1)
        pygame.draw.ellipse(self.screen,(255,255,255), (self.x2 - self.m2/2, self.y2 - self.m2/2, self.m2, self.m2))
        if len(self.px2tab) > 2:
            for i in range (len(self.px2tab) - 1,0, -1):
                pygame.draw.line(self.screen, (255, 0, 255), (self.px2tab[i], self.py2tab[i]), (self.x2tab[i], self.y2tab[i]), 1)
                if len(self.px2tab) >= 100:
                    self.px2tab.pop(0)
                    self.py2tab.pop(0)
                    self.x2tab.pop(0)
                    self.y2tab.pop(0)



        #pygame.draw.line(self.screen, (255, 0, 255), (self.px2, self.py2), (self.x2, self.y2),1)



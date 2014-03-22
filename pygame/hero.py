#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
from blocks import *

HWIDTH = 30
HHEIGHT = 30
HCOLOR = "#3451FF"
SPEEDH = 5
SPEEDV = -8.5
GRAVITY = 0.3
STARTS = 5
INERT = 0.4
PL = False
PR = False
ICON_DIR = os.path.dirname(__file__)

class Hero(sprite.Sprite):
    def __init__(self):
        self.x = 64
        self.y = 64
        self.xspeed = 0
        self.yspeed = STARTS
        self.grav = GRAVITY
        self.ground = False
        self.pr = False
        self.pl = False
        self.inertL = -0.1
        self.inertR = 0.1
        self.rect = Rect((self.x, self.y),(HWIDTH, HHEIGHT))
        self.boxit = Blocks()
        self.platform = self.boxit.box()
        self.hbg = Surface((HWIDTH, HHEIGHT))
        self.hbg.fill(Color(HCOLOR))
        self.bird = image.load("hero/birdD.png")
        self.birdl = image.load("hero/birdL.png")
        self.birdr = image.load("hero/birdR.png")
        self.birdu = image.load("hero/birdU.png")
        self.birdd = image.load("hero/birdD.png")
        self.hbg = image.load("hero/green_bird.png")
        
    def draw(self, screen, x, y):
        for p in self.platform:
            if sprite.collide_rect(self, p):
                if x > 0:
                    self.rect.right = p.rect.left
                if x < 0:
                    self.rect.left = p.rect.right
                if y > 0:
                    self.rect.bottom = p.rect.top
                    self.ground = True
                    self.pl = True
                if y < 0:
                    self.yspeed = 0;
                    self.rect.top = p.rect.bottom         

    def update(self, left, right, up, screen):
                timec = pygame.time.Clock()
                if not self.ground:
                    self.yspeed += GRAVITY
                    if self.hbg == self.birdu:
                        self.hbg = self.birdd
                    elif self.hbg == self.birdd:
                        self.hbg = self.birdu
                self.xspeed = 0
                if self.pl == True:
                    self.inertL = 0
                else:
                    self.inertL = 1
                self.xspeed = self.inertL*self.inertR

                if left:
                    if self.hbg != self.birdl:
                        self.hbg = self.birdl
                    self.xspeed = -SPEEDH
                    self.inertR = -1
                if right:
                    if self.hbg != self.birdr:
                        self.hbg = self.birdr
                    self.xspeed = SPEEDH
                    self.inertR = 1
                if up:
                    if self.ground:
                        self.pl = False
                        self.yspeed = SPEEDV
                        self.ground = False
                        self.inertR = 0
                        self.hbg = self.birdu

                self.rect.y += self.yspeed
                self.draw(screen, 0,self.yspeed)
                self.rect.x += self.xspeed
                timec.tick(50)
                self.draw(screen, self.xspeed, 0)
                screen.blit(self.hbg,(self.rect.left, self.rect.top))

if __name__ == "__main__":
    exit(0)

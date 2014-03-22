#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os
from cross import *
from random import *
import random

BHEIGHT = 32
BWIDTH = 32
BCOLOR = "#000000"
SPICE = " "
DASH = "-"
"""
level = [
           "-------------------------",
           "-                       -",
           "-                       -",
           "-                       -",
           "-            --         -",
           "-                       -",
           "--                      -",
           "-                       -",
           "-                   --- -",
           "-          --           -",
           "-                       -",
           "-      ----             -",
           "-                       -",
           "-   -----------         -",
           "-                       -",
           "-                -      -",
           "-                   --  -",
           "-                       -",
           "-                       -",
           "-------------------------"]
"""
level = []

class Blocks(sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.bbg = Surface((BWIDTH, BHEIGHT))
        self.bbg.fill(Color(BCOLOR))
        self.bbg = image.load("hero/block.jpg")
        self.generate()
        self.coord = []
        self.crossing = []
        for row in level:
            for col in row:
                if col == '-':
                    self.coord.append((self.x, self.y))
                    cr = Cross(self.x, self.y)
                    self.crossing.append(cr)
                self.x += BHEIGHT
            self.y += BWIDTH
            self.x = 0
            
    def genLine(self, i):
        str = ""
        if i == 0 or i == 19:
            for j in xrange(23):
                str = str + DASH
            return str
        else:
            for j in xrange(23):
                x = random.choice(xrange(1,100))
                if 20 < x < 25 or 75 < x < 77:
                    str = str + DASH
                else:
                    str = str + SPICE
            return str;
        
    def  generate(self):
        for i in xrange(20):
            for j in xrange(23):
                str = "-%s-"%(self.genLine(i))
            level.append(str)    
    
    def draw(self, screen):
        for row in self.coord:
            screen.blit(self.bbg, row)
            
    def box(self):
        return self.crossing
    
if __name__ == "__main__":
    exit(0)
        

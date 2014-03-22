#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os

BHEIGHT = 32
BWIDTH = 32

class Cross(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, BWIDTH, BHEIGHT)

if __name__ == "__main__":
    exit(0)

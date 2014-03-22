#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
from blocks import *
from hero import *
from cross import *

HEIGHT = 640
WIDTH = 800
COLOR = "#005500"

def main():
    pygame.init();
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bird")
    bg = Surface((WIDTH, HEIGHT))
    bg.fill(Color(COLOR))
    bg = image.load("hero/back_ground.jpg")
    platform = Blocks()
    player = Hero()
    timer = pygame.time.Clock()
    platform.draw(screen)
    running = True
    left = right = False
    up = False
    while running:
        timer.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Be IDLE friendly

                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   left = True
                if event.key == pygame.K_RIGHT:
                   right = True
                if event.key == pygame.K_UP:
                   up = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                   left = False
                if event.key == pygame.K_RIGHT:
                   right = False
                if event.key == pygame.K_UP:
                   up = False
        screen.blit(bg,(0,0))
        platform.draw(screen)
        player.update(left, right, up, screen)
        pygame.display.update()
    pygame.quit ()

if __name__ == "__main__":
    main()

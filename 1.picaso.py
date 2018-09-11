# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:51:11 2017

@author: ZHENGHAN ZHANG
"""

import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((200, 200, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    pygame.draw.line(screen,(99,99,99),(250,150),(220,80),2)
    pygame.draw.line(screen,(99,99,99),(250,150),(290,50),2)
    pygame.draw.line(screen,(99,99,99),(250,150),(320,180),2)
    pygame.draw.line(screen,(99,99,99),(250,150),(250,300),2)
    pygame.draw.line(screen,(99,99,99),(240,150),(240,300),2)     
    pygame.draw.line(screen,(99,99,99),(260,150),(260,300),2) 
    pygame.draw.circle(screen,(0,0,0),(250,150),66)
    pygame.draw.circle(screen,(144, 144, 144),(230,140),5)
    pygame.draw.circle(screen,(144, 144, 144),(275,115),5)
    pygame.draw.circle(screen,(255, 255, 255),(265,150),20)
    pygame.draw.circle(screen,(0, 0, 0),(265,150),4)
    pygame.draw.circle(screen,(200, 200, 200),(285,170),4)
    pygame.draw.circle(screen,(144,144,144),(255,350),15)
    pygame.draw.rect(screen,(0,0,0),(225,250,50,100))
    pygame.draw.rect(screen,(144,144,144),(225,270,50,5))

    pygame.display.update()

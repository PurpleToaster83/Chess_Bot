import pygame
import sys
import time

import chess as chess

# run the main loop here
pygame.init()
size = width, height = 600, 400

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

# mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
# largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
# moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    pygame.display.flip()
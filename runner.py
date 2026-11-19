import pygame
import sys
import time

import chess
import Board
import Pawn

# run the main loop here
pygame.init()
size = width, height = 600, 400

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

board = Board()
pawns = []
for _ in range(board.get_side()):
    pawns.append(Pawn())

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

#     screen.fill(black)

#     title = largeFont.render("Play Chess", True, white)
#     titleRect = title.get_rect()
#     titleRect.center = ((width / 2), 50)
#     screen.blit(title, titleRect)


#     pygame.display.flip()

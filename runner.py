import pygame
import sys
import time

import chess
from board import Board 
from pawn import Pawn

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

# make the pawns
side = board.get_side()
for c in range(side):
    board.set_loc((side - 2, c), Pawn("white", (side - 2, c)))
    board.set_loc((1, c), Pawn("black", (1, c)))
    print(board)

board.set_loc((0, 0))
board.set_loc((0, side))
board.set_loc((side, 0))
board.set_loc((side, side))


print(board)

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

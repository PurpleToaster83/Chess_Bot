import pygame
import sys
import time
import chess

import chess_logic as cl

pygame.init()
size = width, height = 720, 720

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
board = cl.initial_state()
ai_turn = False

while True:
    clicked = None
    two_player = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = event.pos

    screen.fill(black)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playBButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playB = mediumFont.render("Play as Black", True, black)
        playBRect = playB.get_rect()
        playBRect.center = playBButton.center
        pygame.draw.rect(screen, white, playBButton)
        screen.blit(playB, playBRect)

        playWButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playW = mediumFont.render("Play as White", True, black)
        playWRect = playW.get_rect()
        playWRect.center = playWButton.center
        pygame.draw.rect(screen, white, playWButton)
        screen.blit(playW, playWRect)

        # Check if button is clicked
        if clicked:
            if playBButton.collidepoint(clicked):
                time.sleep(0.2)
                user = cl.W
            elif playWButton.collidepoint(clicked):
                time.sleep(0.2)
                user = cl.B

    else:

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (4 * tile_size),
                       height / 2 - (4 * tile_size))
        tiles = []
        for i in range(8):
            row = []
            for j in range(8):
                piece = board.piece_at(chess.square(j, 7 - i))
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 8)

                if piece:
                    move = moveFont.render(piece.symbol(), True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = cl.terminal(board)
        player = cl.player(board)
        
        # Show title
        if game_over:
            winner = cl.winner(board)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if !two_player:
                if ai_turn:
                    time.sleep(0.5)
                    move = cl.minimax(board)
                    board = cl.result(board, move)
                    ai_turn = False
                else:
                    ai_turn = True

        # Check for a user move
        if clicked and user == player and not game_over:
            for i in range(8):
                for j in range(8):
                    if (board.piece_at(chess.square(j, 7 - i)) == cl.EMPTY and tiles[i][j].collidepoint(clicked)):
                        board = cl.result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 8, height - 65, width / 8, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            if clicked:
                if againButton.collidepoint(mouse):
                    user = None
                    board = cl.initial_state()
                    ai_turn = False

    pygame.display.flip()

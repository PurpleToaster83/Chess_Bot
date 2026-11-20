import pygame
import sys
import time
import chess

import chess_logic as cl

pygame.init()
size = width, height = 720, 800

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
light = (240, 217, 181)
dark = (181, 136, 99)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

tile_size = 80
piece_images = {}
for color in "wb":
    for letter in "KQRBNP":
        piece_images[color + letter] = pygame.image.load_sized_svg(
            f"pieces/{color}{letter}.svg", (tile_size, tile_size)
        )

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)

user = None
board = cl.initial_state()
ai_turn = False
two_player = True # change this
selected = None


while True:
    clicked = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = event.pos

    screen.fill(black)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Play Chess", True, white)
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
        pygame.draw.rect(screen, (white), playWButton)
        screen.blit(playW, playWRect)

        # Check if button is clicked
        if clicked:
            if playBButton.collidepoint(clicked):
                time.sleep(0.2)
                user = cl.B
            elif playWButton.collidepoint(clicked):
                time.sleep(0.2)
                user = cl.W

    else:

        # Draw game board
        tile_origin = (width / 2 - (4 * tile_size),
                       height / 2 - (4 * tile_size))
        for i in range(8):
            for j in range(8):
                piece = board.piece_at(chess.square(j, 7 - i))
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                color = light if (i + j) % 2 == 0 else dark
                pygame.draw.rect(screen, color, rect)
                if selected == chess.square(j, 7 - i):
                    pygame.draw.rect(screen, (246, 246, 105), rect, 4)

                if piece:
                    key = ("w" if piece.color == chess.WHITE else "b") + piece.symbol().upper()
                    screen.blit(piece_images[key], rect)

        game_over = cl.terminal(board)
        player = cl.player(board)
        
        # Show title
        if game_over:
            winner = cl.winner(board)
            if winner is None:
                title = f"Game Over: Draw."
            else:
                title = f"Game Over: {'White' if winner else 'Black'} wins."
        elif two_player or user == player:
            title = f"{'White' if board.turn else 'Black'} to move"
            if board.is_check():
                title += " (check)"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if not two_player:
                if ai_turn:
                    time.sleep(0.5)
                    move = cl.minimax(board)
                    board.push(move)
                    ai_turn = False
                else:
                    ai_turn = True

        # Check for a user move
        if clicked and (two_player or user == player) and not game_over:
            # Work out which square was clicked
            x, y = clicked
            j = int((x - tile_origin[0]) // tile_size)
            i = int((y - tile_origin[1]) // tile_size)
            if 0 <= i < 8 and 0 <= j < 8:
                sq = chess.square(j, 7 - i)
                piece = board.piece_at(sq)

                if selected is None:
                    # First click: pick up one of your own pieces
                    if piece and piece.color == board.turn:
                        selected = sq
                else:
                    # Second click: try to move there
                    move = chess.Move(selected, sq)
                    if move not in board.legal_moves:
                        move = chess.Move(selected, sq, promotion=chess.QUEEN)
                    if move in board.legal_moves:
                        board.push(move)
                        selected = None
                    elif piece and piece.color == board.turn:
                        selected = sq   # clicked another of your pieces: switch to it
                    else:
                        selected = None  # illegal target: drop the selection

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            if clicked:
                if againButton.collidepoint(clicked):
                    user = None
                    board = cl.initial_state()
                    ai_turn = False
                    selected = None

    pygame.display.flip()
    clock.tick(30)

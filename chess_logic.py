"""
Tic Tac Toe Player
"""

import copy
import chess

W = chess.WHITE
B= chess.BLACK
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return chess.Board()

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return board.turn

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return list(board.legal_moves)

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    b = board.copy(stack=False)
    b.push(action)
    return b

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return board.outcome().winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return board.is_game_over()

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

#adapted from lecture 0's slideshow (slides #285, #286)

    #function to maximize score
    def max_value(board, alpha, beta):

        #check if the board is already a terminal case
        if terminal(board):
            return (utility(board), None, float('inf'), utility(board))

        v = float('-inf')

        for action in actions(board):
            minimum = min_value(result(board, action), alpha, beta) #call min_value to search deeper
            if minimum[0] > v:
                v = minimum[0]

                #perform alpha-beta pruning
                alpha = max(minimum[2], minimum[3], alpha)
                best = action

                #check for prune case
                if alpha >= beta:
                    break

        return (v, best, alpha, beta)

    #function to minimize score
    def min_value(board,alpha, beta):

        #check if the board is already a terminal case
        if terminal(board):
            return (utility(board), None, utility(board), float('-inf'))

        v = float('inf')

        for action in actions(board):
            maximum = max_value(result(board, action), alpha, beta) #call max_value to search deeper
            if maximum[0] < v:
                v = maximum[0]

                #perform alpha-beta pruning
                beta = min(maximum[2], maximum[3], beta)
                best = action

                #check for prune case
                if alpha >= beta:
                    break

        return (v, best, alpha, beta)

    if terminal(board):
        return None

    #call max_val or min_val first if X or O
    if player(board) == X:
        move = max_value(board, float('-inf'), float('inf'))
        return move[1]

    if player(board) == O:
        move = min_value(board, float('-inf'), float('inf'))
        return move[1]

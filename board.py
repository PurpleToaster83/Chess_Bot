class Board:
    def __init__(self):
        self.side = 8
        self.board = [([0] * self.side)] * self.side

    def get_board(self):
        return self.board

    def get_side(self):
        return self.side

    def empty(self, loc):
        return self.board[loc[0]][loc[1]] == 0

    def set_loc(self, loc, piece):
        self.board[loc[0]][loc[1]] = piece

    def __str__(self):
        pass #TODO
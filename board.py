class Board:
    def __init__(self):
        self.side = 8
        self.board = [
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0]
        ]

    def get_board(self):
        return self.board

    def get_side(self):
        return self.side

    def empty(self, loc):
        return self.board[loc[0]][loc[1]] == 0

    def set_loc(self, loc, piece):
        b = loc[1]
        self.board[loc[0]][loc[1]] = piece        

    def __str__(self):
        to_print = ""
        for i in range(self.side):
            for j in range(self.side):
                if self.board[i][j]:
                    to_print += self.board[i][j].get_char()
                else:
                    to_print += "0"
            to_print += "\n"
        return to_print
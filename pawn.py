class Pawn:
    def __init__(self, side, loc):
        self.side = side
        self.char = "p"
        self.loc = self.r, self.c = loc

    def get_moves(self, state):
        if state.empty((self.r + 1, self.c)):
            return (self.r - 1, self.c)

    def get_char(self):
        return self.char

    def get_loc(self):
        return self.loc

    def set_loc(self, new_loc):
        self.loc = new_loc
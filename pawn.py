class pawn:
    def __init__(self, side, loc):
        self.side = side
        self.char = "p"
        self.loc = self.x, self.y = loc

    def get_moves(self, state):
        if state.empty((self.y, self.x + 1)):
            return (self.y, self.x + 1)

    def get_loc(self):
        return self.loc

    def set_loc(self, new_loc):
        self.loc = new_loc
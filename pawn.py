class pawn:
    def __init__(self, side, loc):
        self.side = side
        self.loc = self.x, self.y = loc

    def get_moves(self, state):
        
        if state[self.y][self.x + 1].empty():
            return (self.y, self.x + 1)

    def get_loc(self):
        return self.loc

    def set_loc(self, new_loc):
        self.loc = new_loc
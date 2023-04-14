class Piece:
    def __init__(self, x, y, clr):
        self.x = x
        self.y = y
        self.clr = clr
    
    def move_to(self, x1, y1):
        if not Piece.is_legal_move(x1, y1):
            return False
        return True

    @staticmethod
    def is_legal_move(x1, y1):
        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
            return True
        return False
    
    # def any_on_path(self, x1, y1, board):
    #     return False

    def __eq__(self, other):
        if isinstance(other, Piece):
            return self.get_clr() == other.get_clr()
        else:
            return None
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_clr(self):
        return self.clr
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
        
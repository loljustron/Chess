from .piece import Piece


class Pawn(Piece):
    def __init__(self, x, y, clr):
        super().__init__(x, y, clr)

    def move_to(self, x1, y1, board):
        if not super().move_to(x1, y1):
            return False
        
        if (((self.get_x() == x1) and (y1 - self.get_y() == 1 and self.get_clr() == 1) or
                (self.get_y() - y1  == 1 and self.get_clr() == 0) or
                (self.get_y() == 1 and y1 == 3 and self.get_clr() == 1) or
                (self.get_y() == 6 and y1 == 4 and self.get_clr() == 0)) or
                
                ((self.get_y() - y1  == 1 and self.get_clr() == 0 or
                (y1 - self.get_y() == 1 and self.get_clr() == 1)) and
                abs(self.get_x() - x1) == 1 and board[y1][x1] != self)):
            self.set_x(x1)
            self.set_y(y1)
            return True
        else:
            return False
    
    def __str__(self):
        return('♙' if self.get_clr() == 1 else '♟')
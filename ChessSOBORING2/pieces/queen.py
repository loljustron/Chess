from .piece import Piece
from .bishop import Bishop
from .rook import Rook


class Queen(Piece):
    def __init__(self, x, y, clr):
        super().__init__(x, y, clr)

    def move_to(self, x1, y1, board):
        if not super().move_to(x1, y1):
            return False

        if (abs(self.get_x() - x1) == abs(self.get_y() - y1)):
            if Bishop.check_bishops_move(self.get_x(), self.get_y(), x1, y1, board):
                self.set_x(x1)
                self.set_y(y1)
                return True
            return False
        elif (self.get_x() == x1 or self.get_y() == y1):
            if Rook.check_rooks_move(self.get_x(), self.get_y(), x1, y1, board):
                self.set_x(x1)
                self.set_y(y1)
                return True
            return False
        else:
            return False    

    def __str__(self):
        return '♕' if self.get_clr() == 1 else '♛'
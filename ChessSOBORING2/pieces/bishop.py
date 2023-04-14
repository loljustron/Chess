from .piece import Piece


class Bishop(Piece):
    def __init__(self, x, y, clr):
        super().__init__(x, y, clr)

    def move_to(self, x1, y1, board):
        if not super().move_to(x1, y1):
            return False
        
        if (abs(self.get_x() - x1) == abs(self.get_y() - y1)):
            if self.check_bishops_move(self.get_x(), self.get_y(), x1, y1, board):
                self.set_x(x1)
                self.set_y(y1)
                return True
            return False
        else:
            return False

    @staticmethod
    def check_bishops_move(x0 : int, y0 : int, x1 : int, y1 : int, board : list):
        # if 
        y_changes = int((y1 - y0) / abs(y1 - y0))
        x_changes = int((x1 - x0) / abs(x1 - x0))
        for i in range(1, abs(x1 - x0)):
            if isinstance(board[y0 + i * y_changes][x0 + i * x_changes], Piece):
                return False
        return True
    
    def __str__(self):
        return '♗' if self.clr == 1 else '♝'
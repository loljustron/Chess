from .piece import Piece


class Rook(Piece):
    def __init__(self, x, y, clr):
        super().__init__(x, y, clr)

    def move_to(self,x1, y1, board):
        if not super().move_to(x1, y1):
            return False
        
        if self.get_x() == x1 or self.get_y() == y1:
            if Rook.check_rooks_move(self.get_x(), self.get_y(), x1, y1, board):
                self.set_x(x1)
                self.set_y(y1)
                return True
            return False
        else:
            return False
        
    @staticmethod
    def check_rooks_move(x0 : int, y0 : int, x1 : int, y1 : int, board : list):
        if x0 == x1:
            for i in range(y0 + 1, y1):
                if isinstance(board[i][x0], Piece):
                    return False
        if y0 == y1:
            for i in range(x0 + 1, x1):
                if isinstance(board[y0][i], Piece):
                    return False
        return True
        # if isinstance(board[y1][x1])
    
    def __str__(self):
        return '♖' if self.get_clr() == 1 else '♜'
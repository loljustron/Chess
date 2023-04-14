from pieces import Bishop, Queen, Rook, Pawn, King, Knight, Piece


class Board:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.place_pieces()
    
    def place_pieces(self):
        # Place Pawns
        for i in range(8):
            self.board[1][i] = Pawn(i, 1, 1)
        for i in range(8):
            self.board[6][i] = Pawn(i, 6, 0)
        
        self.place_em(0, 1)
        self.place_em(7, 0)
            
        
    def place_em(self, y, clr):
        # Place Rooks
        self.board[y][0] = Rook(0, y, clr)
        self.board[y][7] = Rook(7, y, clr)

        # Place Knights
        self.board[y][1] = Knight(1, y, clr)
        self.board[y][6] = Knight(6, y, clr)

        # Place Bishops
        self.board[y][2] = Bishop(2, y, clr)
        self.board[y][5] = Bishop(5, y, clr)

        # Place Queens and Kings
        self.board[y][3] = Queen(3, y, clr)
        self.board[y][4] = King(4, y, clr)
    
    def move_piece(self, x0, y0, x1, y1):
        if not isinstance(self.board[y0][x0], Piece):
            return 'There is no piece'
        if self.board[y0][x0].move_to(x1, y1, self.board):
            if (not isinstance(self.board[y1][x1], Piece) or
            self.board[y1][x1] != self.board[y0][x0]):
                self.board[y1][x1] = self.board[y0][x0]
                self.board[y0][x0] = 0
                return True
            else:
                return False
        else:
            return False
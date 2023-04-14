from board import Board
from pieces import Piece


letters_dict = {'a' : 1, 'b' : 2, 'c' : 3,
                'd' : 4, 'e' : 5, 'f' : 6,
                'g' : 7, 'h' : 8}


def ask_move():
    while True:
        starting_pos = input('\nEnter the starting position of the piece: ').split()
        final_pos = input('Enter where to place that piece: ').split()

        try:
            starting_pos = tuple(map(int, starting_pos))
            final_pos = input('\nEnter where to place that piece: ').split()
        except:
            try:
                starting_pos[0] = letters_dict[starting_pos[0].lower()]
                final_pos[0] = letters_dict[final_pos[0].lower()]
                starting_pos = tuple(map(lambda x: int(x) - 1, starting_pos))
                final_pos = tuple(map(lambda x: int(x) - 1, final_pos))
            except:
                print('\nPlease, try entering positions once again')
                continue
        
        # for i in starting_pos + final_pos:
        #     if not 1 >= i >= 8:
        #         continue

        return starting_pos + final_pos

def make_move(move, board : Board):
    if board.move_piece(*move):
        return True
    else:
        print('\nWrong move, try again.')
    

def intro_txt():
    intro = '''\nHey, if you want to play chess, I could easily help you!
I would be a guide throught your play. Just follow my instructions!'''
    return intro

def instr_txt():
    instr = '''\nIn your moves, you have to write position of a
figure, and where you wanna place it. The field is 8 x 8, so write positions in the range of
[A - H] or [1 - 8]. Writing a letter of a column and a number of a row (ie 'A 3', 'C 5', 'E 8'),
or just two numbers, a column and a row (i e '1 5', '2 7' '3 1').'''
    return instr

def still_alive(board):
    white = False
    black = False
    for row in board:
        for i in row:
            if isinstance(i, Piece):
                if i.get_clr() == 0:
                    black = True
                else:
                    white = True
                if black and white:
                    break
    return 'Black' * black + ' ' * (black and white) + 'White' * white

def show_plate(board):
    for i in range(7, -1, -1):
        for j in range(8):
            print(board.board[i][j], end=' ')
        print()
    
def main():
    board = Board()
    clr = 1
    print(intro_txt())
    print(instr_txt())
    print()
    show_plate(board)
    
    while still_alive(board.board) == 'Black White':
        print('\n' + ("Black's" if clr == 0 else "White's") + ' move:')
        move = ask_move()
        if isinstance(board.board[move[1]][move[0]], Piece):
            if board.board[move[1]][move[0]].get_clr() == clr:
                if make_move(move, board):
                    show_plate(board)
                    clr = 0 if clr == 1 else 1
            else:
                print('Wrong move, its now ' + ("black's" if clr == 0 else "white's") + ' move')
        else:
            print('\nPlease, try entering positions once again')

main()
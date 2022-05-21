import pygame
from bobail.constants import COLS, ROWS, YELLOW, BLUE, BROWN, WHITE, BLACK, SQUARE_SIZE
from bobail.piece import Piece



class Board:
    def __init__(self):
        self.board = []
        self.create_board()

    def draw_background(self, win):
        win.fill(BROWN)

    def draw_circles(self, win):
        radius = SQUARE_SIZE // 2 - 16
        for row in range(ROWS):
            for col in range(COLS):
                x = SQUARE_SIZE * col + SQUARE_SIZE // 2
                y = SQUARE_SIZE * row + SQUARE_SIZE // 2
                pygame.draw.circle(win, BLACK, (x, y), radius)

    def evaluate(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if piece != 0 and piece.color == WHITE:
                    return row

    def evaluate2(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if piece != 0 and piece.color == WHITE:
                    return self.valid_moves(piece)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)

    def get_piece(self, row, col):
        try:
            return self.board[row][col]
        except IndexError:
            print("indexerror")

    def get_piece2(self, row, col):
        try:
            return self.board[row][col]
        except IndexError:
            return True

    def winner(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if piece != 0 and piece.color == WHITE:
                    if row == 0:
                        print("Yellow wins!")
                        return YELLOW
                    if row == 4:
                        print("Blue wins!")
                        return BLUE
        return None

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0:
                    self.board[row].append(Piece(row, col, YELLOW))
                elif row == 4:
                    self.board[row].append(Piece(row, col, BLUE))
                elif row == 2 and col == 2:
                    self.board[row].append(Piece(row, col, WHITE))
                else:
                    self.board[row].append(0)


    def draw(self, win):
        self.draw_background(win)
        self.draw_circles(win)
        for row in range(ROWS):
            for col in range (COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)


    def valid_moves(self, piece):
        x = piece.row
        y = piece.col
        moves = []
        rows = []
        cols = []
        if piece.color == WHITE:
            for row in range(ROWS):
                if (x - row) in range(-1, 2):
                    rows.append(row)
            for col in range(COLS):
                if (col - y) in range(-1, 2):
                    cols.append(col)
            for row in rows:
                for col in cols:
                    piece = self.get_piece(row, col)
                    if piece == 0:
                        moves.append((row, col))

        else:

            # Up
            upwards = []
            upwards_temp = []
            for i in range(1, x + 2):
                row = x - i
                col = y
                if row >= 0:
                    piece = self.get_piece2(row, col)
                    # If field is empty
                    if piece == 0:
                        upwards_temp.append((row, col))
                    # If field is occupied by another piece
                    else:
                        try:
                            upwards.append(upwards_temp.pop())
                            moves.append(upwards[0])
                            break
                        except IndexError:
                            break
                else:
                    try:
                        upwards.append(upwards_temp.pop())
                        moves.append(upwards[0])
                        break
                    except IndexError:
                        break
            # Down
            downwards = []
            downwards_temp = []
            for i in range(1, 6 - x):
                row = x + i
                col = y
                piece = self.get_piece2(row, col)
                # seems like it doesn't need the option of going out of range
                if piece == 0:
                    downwards_temp.append((row, col))
                else:
                    try:
                        downwards.append(downwards_temp.pop())
                        moves.append(downwards[0])
                    except IndexError:
                        break

            # Left
            left = []
            left_temp = []
            for i in range(1, y + 2):
                row = x
                col = y - i
                if col >= 0:
                    piece = self.get_piece2(row, col)
                    if piece == 0:
                        left_temp.append((row, col))
                    else:
                        try:
                            left.append(left_temp.pop())
                            moves.append(left[0])
                            break
                        except IndexError:
                            break
                else:
                    try:
                        left.append(left_temp.pop())
                        moves.append(left[0])
                        break
                    except IndexError:
                        break

            # Right
            right = []
            right_temp = []
            for i in range(1, 6 - y):
                row = x
                col = y + i
                piece = self.get_piece2(row, col)
                if piece == 0:
                    right_temp.append((row, col))
                else:
                    try:
                        right.append(right_temp.pop())
                        moves.append(right[0])
                        break
                    except IndexError:
                        break

            # Up and right
            upright = []
            upright_temp = []
            for i in range(1, 6 - y):
                row = x - i
                col = y + i
                if row >= 0:
                    piece = self.get_piece2(row, col)
                    if piece == 0:
                        upright_temp.append((row, col))
                    else:
                        try:
                            upright.append(upright_temp.pop())
                            moves.append(upright[0])
                            break
                        except IndexError:
                            break
                else:
                    try:
                        upright.append(upright_temp.pop())
                        moves.append(upright[0])
                        break
                    except IndexError:
                        break

            # Up and left
            upleft = []
            upleft_temp = []
            for i in range(1, y + 2):
                row = x - i
                col = y - i
                if col >= 0 and row >= 0:
                    piece = self.get_piece2(row, col)
                    if piece == 0:
                        upleft_temp.append((row, col))
                    else:
                        try:
                            upleft.append(upleft_temp.pop())
                            moves.append(upleft[0])
                            break
                        except IndexError:
                            break
                else:
                    try:
                        upleft.append(upleft_temp.pop())
                        moves.append(upleft[0])
                        break
                    except IndexError:
                        break

            # Down and right
            downright = []
            downright_temp = []
            for i in range(1, 6 - x):
                row = x + i
                col = y + i
                piece = self.get_piece2(row, col)
                if piece == 0:
                    downright_temp.append((row, col))
                else:
                    try:
                        downright.append(downright_temp.pop())
                        moves.append(downright[0])
                    except IndexError:
                        break

            # Down and left
            downleft = []
            downleft_temp = []
            for i in range(1, y + 2):
                row = x + i
                col = y - i
                if col >= 0:
                    piece = self.get_piece2(row, col)
                    if piece == 0:
                        downleft_temp.append((row, col))
                    else:
                        try:
                            downleft.append(downleft_temp.pop())
                            moves.append(downleft[0])
                            break
                        except IndexError:
                            break
                else:
                    try:
                        downleft.append(downleft_temp.pop())
                        moves.append(downleft[0])
                        break
                    except IndexError:
                        break

        return moves

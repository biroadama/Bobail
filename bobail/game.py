import pygame
from .constants import YELLOW, BLUE, WHITE, SQUARE_SIZE, ROWS, COLS
from .board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.draw_selectable(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.ai_turn = False
        self.valid_moves = {}

    def reset(self):
        self._init()

    def winner(self):
        return self.board.winner()


    def winner2(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.get_piece(row, col)
                if piece != 0 and self.turn == WHITE and self.selected and self.valid_moves == []:
                    self.change_turn()
                    if self.turn == BLUE:
                        print('Yellow wins!')
                        return YELLOW
                    if self.turn == YELLOW:
                        print('Blue wins!')
                        return BLUE
        return None


    def draw_selectable(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                x = SQUARE_SIZE * col + SQUARE_SIZE // 2
                y = SQUARE_SIZE * row + SQUARE_SIZE // 2
                piece = self.board.get_piece(row, col)
                if piece != 0 and piece.color == self.turn:
                    pygame.draw.circle(win, (138, 201, 38), (x, y), 22, 2)


    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.valid_moves(piece)
            return True

        self.selected = None
        self.valid_moves = {}
        return False


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False

        return True


    def change_turn(self):
        if self.ai_turn == False:
            if self.turn == WHITE:
                self.turn = BLUE
                return

            if self.turn == BLUE:
                self.turn = WHITE
                self.ai_turn = True
                print("Yellow player's turn")
                return

        if self.ai_turn == True:
            if self.turn == WHITE:
                self.turn = YELLOW
                return

            if self.turn == YELLOW:
                self.turn = WHITE
                self.ai_turn = False
                print("Blue player's turn")
                return


    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 10)


    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()


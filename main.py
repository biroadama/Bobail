import pygame
from bobeil.constants import WIDTH, HEIGHT, SQUARE_SIZE, YELLOW, BLUE, WHITE
from bobeil.game import Game
from minimax.algorithm import minimax


pygame.init()

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bobail')
row = col = 5
print("Blue player's turn")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        # if game.ai_turn is True:
        #     value, new_board = minimax(game.get_board(), 3, True, game.turn, game)
        #     print(new_board)
        #     print(game.ai_turn)
        #     game.ai_move(new_board)

        if game.winner() != None:
            run = False

        if game.winner2() != None:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)

        game.update()

main()
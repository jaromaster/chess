import pygame
from Pieces.Pawn import Pawn
from board import Board

# create pygame window with size, title and color
# returns screen
def initWindow(width, height, title, color):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    screen.fill(color)
    pygame.display.flip()

    return screen

# places all the chess pieces on the board
def initChessPieces(board: Board):
    width = len(board.matrix[0])

    for x in range(width):
        pawn = Pawn("black", board.matrix, pos=(x, 1))
        board.setChessPiece(pawn, 1, x)

    for x in range(width):
        pawn = Pawn("white", board.matrix, pos=(x, 6))
        board.setChessPiece(pawn, 6, x)

# main function
def main():
    width, height, title = 800, 600, "Chess"
    background_color = (255, 255, 255)
    gameBoard = Board(8, 8)
    initChessPieces(gameBoard)

    screen = initWindow(width, height, title, background_color)
    gameBoard.drawGrid(screen)
    gameBoard.drawPieces(screen)

    # game loop
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # break if quit event occured
                isRunning = False
    


if __name__ == "__main__":
    main()
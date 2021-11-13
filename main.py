import time
import pygame
from Board import Board

# create pygame window with size, title and color
def initWindow(width, height, title, color) -> pygame.Surface:
    """ initialize new pygame window with size, title, color """
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    screen.fill(color)
    pygame.display.flip()

    return screen

# main function
def main():
    """ main function contains all the game logic """
    # game variables
    width, height, title = 800, 600, "Chess"
    background_color = (255, 255, 255)
    squareLength = 70
    squareColor = (111, 73, 73)
    mouseCol, mouseRow = 0, 0
    selectedField = None
    
    # initialize game window
    screen = initWindow(width, height, title, background_color) 
    
    # game board
    gameBoard = Board(8, 8, squareLength, squareColor, screen) # 8x8 board
    gameBoard.initChessPieces() # initialize chess pieces
    gameBoard.drawGrid() # draw grid
    gameBoard.drawPieces() # draw all chess pieces on grid

    # game loop
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # break if quit event occurred
                isRunning = False

            elif event.type == pygame.MOUSEBUTTONDOWN: # user clicked
                # convert coordinates of mouse to rows and columns of grid
                mouseCol = (pygame.mouse.get_pos()[0] - gameBoard.xStart) // squareLength
                mouseRow = (pygame.mouse.get_pos()[1] - gameBoard.yStart) // squareLength
                mouseCol = int(mouseCol)
                mouseRow = int(mouseRow)
                # if selected square in grid, update selectedField
                if gameBoard.inBounds(mouseCol, mouseRow):
                    # redraw gameBoard
                    gameBoard.drawGrid()
                    gameBoard.drawPieces()
                    # update selectedField
                    selectedField = gameBoard.matrix[mouseRow, mouseCol]
                    # highlight possible moves if chess piece selected
                    moves = selectedField.validMoves() if selectedField else []
                    gameBoard.highlightMoves(moves)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
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
    width, height, title = 1000, 800, "Chess"
    background_color = (255, 255, 255)
    squareLength = 80
    squareColor = (111, 73, 73)
    
    # initialize game window
    screen = initWindow(width, height, title, background_color) 
    
    # game board
    gameBoard = Board(squareLength, squareColor, screen) # 8x8 board
    gameBoard.drawGrid()
    gameBoard.drawChessPieces() # draw all chess pieces on grid

    isRunning = True
    selectedField = None
    turn = "white"
    mouseCol, mouseRow = 0, 0
    moves = set() # possible moves of selected chess piece
    # game loop
    pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN])
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # break if quit event occurred
                isRunning = False

            elif event.type == pygame.MOUSEBUTTONDOWN: # user clicked
                # convert coordinates of mouse to rows and columns of grid
                mouseCol = int((pygame.mouse.get_pos()[0] - gameBoard.xStart) // squareLength)
                mouseRow = int((pygame.mouse.get_pos()[1] - gameBoard.yStart) // squareLength)
                # if selected square in grid, update selectedField
                if gameBoard.inBounds(mouseCol, mouseRow):
                    # if player wants to move chess piece
                    x,y = mouseCol, mouseRow
                    drawMoves = True
                    if selectedField and (x, y) in moves and selectedField.color == turn: # make move if selectedField is chess piece and has player's color              
                        selectedField.moveTo(x, y) # move chess piece to new position

                        # check for wins after every move
                        if not gameBoard.checkBothKingsAlive():
                            print("King dead")
                            #todo: winning screen, restart game
                        
                        moves = set() # reset moves
                        turn = "white" if turn == "black" else "black" # switch color
                        drawMoves = False
                    
                    # redraw gameBoard
                    gameBoard.drawGrid()
                    gameBoard.drawChessPieces()

                    # update selectedField
                    selectedField = gameBoard.grid[mouseRow, mouseCol]
                    # highlight possible moves if chess piece selected
                    if drawMoves and selectedField and selectedField.color == turn:
                        moves = set(selectedField.validMoves()) if selectedField else set()
                        gameBoard.highlightMoves(moves)

        time.sleep(0.001) # delay

if __name__ == "__main__":
    main()
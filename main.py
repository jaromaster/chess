import time
import pygame
from Board import Board

# create pygame window with size, title and color
def initWindow(width, height, title, color) -> pygame.Surface:
    """ initialize new pygame window with size, title, color """
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    screen.fill(color)

    return screen

# write text with specific font to specific position 
def writeText(string, xCenter, yCenter, font, screen):
    """ draw text to canvas, call pygame.display.update() to update screen """
    winnerText = font.render(string, True, (0,0,0), (255,255,255)) # tuples are colors of text and background
    winnerTextRect = winnerText.get_rect()
    winnerTextRect.centerx = xCenter
    winnerTextRect.centery = yCenter
    screen.blit(winnerText, winnerTextRect)

# main function
def main():
    """ main function contains all the game logic """
    pygame.init()
    width, height, title = 1000, 800, "Chess"
    background_color = (255, 255, 255)
    squareColor = (111, 73, 73)
    squareLength = 80
    fontSize = 30
    font = pygame.font.Font("freesansbold.ttf", fontSize) # create font
    
    # initialize game window
    screen = initWindow(width, height, title, background_color) 
    
    # game board
    gameBoard = Board(squareLength, squareColor, screen)
    gameBoard.drawGrid()
    gameBoard.drawChessPieces()

    isRunning = True
    selectedField = None
    turn = "white"
    mouseCol, mouseRow = 0, 0
    moves = set() # possible moves of selected chess piece
    won = False # disable clicking if player won
    # game loop
    pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN])
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # break if quit event occurred
                isRunning = False

            elif event.type == pygame.KEYDOWN: 
                # restart game by pressing space
                if event.key == pygame.K_SPACE:
                    won = False
                    turn = "white"
                    screen.fill(pygame.Color("white")) # redraw background
                    gameBoard.initChessPieces()
                    gameBoard.drawGrid()
                    gameBoard.drawChessPieces()

            elif event.type == pygame.MOUSEBUTTONDOWN and not won: # user clicked, disable if player already won
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
                        bothAlive, colorDead = gameBoard.checkBothKingsAlive()
                        if not bothAlive: # if king dead
                            won = True

                            # display winner text
                            textFieldHeight = (height - 8*squareLength) // 2 # center text vertically in area outside grid
                            color = "black" if colorDead == "white" else "white"
                            writeText(color.capitalize()+" won", width // 2, textFieldHeight // 2, font, screen)
                            # display text explaining how to restart
                            writeText("Press SPACE to restart", width // 2, height - textFieldHeight // 2, font, screen)
                            pygame.display.update()

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
from numpy.lib.utils import get_include
import pygame
from board import Board

# create pygame window with size, title and color
# returns screen
def initWindow(width, height, title, color):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    screen.fill(color)
    pygame.display.flip()

    return screen

# draw grid using black and white squares
def drawGrid(gridShape, screen):
    sideLength = 40
    width, height = screen.get_size()

    # xStart and yStart are used for centering the grid
    xStart = (width - gridShape[0] * sideLength) / 2
    yStart = (height - gridShape[1] * sideLength) / 2

    isWhite = True
    for i in range(gridShape[0]):
        for j in range(gridShape[1]):
            x = j * sideLength
            y = i * sideLength

            square = pygame.Rect(x + xStart, y + yStart, sideLength, sideLength)
            if isWhite:
                pygame.draw.rect(screen, (255,255,255), square) # white
            else:
                pygame.draw.rect(screen, (0,0,0), square) # black
            
            isWhite = not isWhite # switch black and white
        isWhite = not isWhite # after line break: switch again

    # draw rectangle around grid
    square = pygame.Rect(xStart, yStart, gridShape[0] * sideLength, gridShape[1] * sideLength)
    pygame.draw.rect(screen, (0,0,0), square, 2)

    pygame.display.flip() # display



# main function
def main():
    width, height, title = 800, 600, "Chess"
    background_color = (255, 255, 255)
    gameBoard = Board(8, 8)

    screen = initWindow(width, height, title, background_color)
    drawGrid(gameBoard.getSize(), screen)
    

    # game loop
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # break if quit event occured
                isRunning = False
    


if __name__ == "__main__":
    main()
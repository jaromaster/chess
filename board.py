import numpy as np
import pygame
from Pieces.Pawn import Pawn


# board is used to interact with the chess board
class Board:
    def __init__(self, numRows, numCols, squareLength = 70):
        self.matrix = np.empty((numRows, numCols), dtype="object")
        self.squareLength = squareLength

    # set specific chess piece to position on board, else return
    def setChessPiece(self, chessPiece, row, col):
        if (row < len(self.matrix) and col < len(self.matrix[0]) and row >= 0 and col >= 0):
            self.matrix[row, col] = chessPiece

    # return board size
    def getSize(self):
        return self.matrix.shape

    # draw grid using colored squares
    def drawGrid(self, screen):
        width, height = screen.get_size()
        cols, rows = self.matrix.shape


        # xStart and yStart are used for centering the grid
        xStart = (width - cols * self.squareLength) / 2
        yStart = (height - rows * self.squareLength) / 2
        # color of non-white squares
        squareColor = (111, 73, 73)

        isWhite = True
        for i in range(rows):
            for j in range(cols):
                x = j * self.squareLength
                y = i * self.squareLength

                square = pygame.Rect(x + xStart, y + yStart, self.squareLength, self.squareLength)
                if isWhite:
                    pygame.draw.rect(screen, (255,255,255), square) # white
                else:
                    pygame.draw.rect(screen, squareColor, square) # colored
                
                isWhite = not isWhite # switch black and white
            isWhite = not isWhite # after line break: switch again

        # draw rectangle around grid
        square = pygame.Rect(xStart, yStart, cols * self.squareLength, rows * self.squareLength)
        pygame.draw.rect(screen, squareColor, square, 2)

        pygame.display.flip() # display

    # draw board to given screen
    def drawPieces(self, screen):
        width, height = screen.get_size()
        cols, rows = self.matrix.shape

        # xStart and yStart are used for centering the grid
        xStart = (width - cols * self.squareLength) / 2
        yStart = (height - rows * self.squareLength) / 2

        for i in range(rows):
            for j in range(cols):
                x = j * self.squareLength
                y = i * self.squareLength
                
                if isinstance(self.matrix[i, j], Pawn):
                    # pawnImage = pygame.image.load("./Assets/pawn.jpeg")
                    # screen.blit(pawnImage, (x+xStart, y+yStart))
                    pygame.draw.circle(screen, (0,0,0), (x+xStart+self.squareLength/2,y+yStart+self.squareLength/2), self.squareLength/2) # draw black circle if pawn (for testing)

        pygame.display.flip()


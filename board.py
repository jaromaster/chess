import numpy as np
import pygame
from Pieces.Pawn import Pawn

# board is used to interact with the chess board
class Board:
    def __init__(self, numRows, numCols, squareLength, squareColor, screen):
        self.matrix = np.empty((numRows, numCols), dtype="object")
        self.screen = screen
        # side length of the squares
        self.squareLength = squareLength

        # color of non-white squares
        self.squareColor = squareColor
        self.highlightColor = (0, 200, 0)

        width, height = screen.get_size()
        cols, rows = self.matrix.shape
        # xStart and yStart are used for centering the grid
        self.xStart = (width - cols * self.squareLength) / 2
        self.yStart = (height - rows * self.squareLength) / 2


    # if position is in bounds return true, else false
    def inBounds(self, x, y):
        gridWidth, gridHeight = self.matrix.shape

        return (x >= 0 and y >= 0 and x < gridWidth and y < gridHeight)

    # places all the chess pieces on the board
    def initChessPieces(self):
        width = len(self.matrix[0])

        # place all pawns
        for col in range(width):
            pawn = Pawn("black", self.matrix, (col, 1), self.screen)
            self.setChessPiece(pawn, 1, col)

        for col in range(width):
            pawn = Pawn("white", self.matrix, (col, 6), self.screen)
            self.setChessPiece(pawn, 6, col)

    # set specific chess piece to position on board, else return
    def setChessPiece(self, chessPiece, row, col):
        if self.inBounds(col, row):
            self.matrix[row, col] = chessPiece

    # return board size
    def getSize(self):
        return self.matrix.shape

    # draw grid using colored squares
    def drawGrid(self):
        cols, rows = self.matrix.shape

        isWhite = True
        for i in range(rows):
            for j in range(cols):
                x = j * self.squareLength
                y = i * self.squareLength

                square = pygame.Rect(x + self.xStart, y + self.yStart, self.squareLength, self.squareLength)
                if isWhite:
                    pygame.draw.rect(self.screen, (255,255,255), square) # draw white cell
                else:
                    pygame.draw.rect(self.screen, self.squareColor, square) # draw colored cell
                
                isWhite = not isWhite # switch black and white
            isWhite = not isWhite # after line break: switch again

        # draw square around grid
        square = pygame.Rect(self.xStart, self.yStart, cols * self.squareLength, rows * self.squareLength)
        pygame.draw.rect(self.screen, self.squareColor, square, 2)

        pygame.display.flip() # display

    # draw all pieces on board
    def drawPieces(self):
        width, height = self.screen.get_size()
        cols, rows = self.matrix.shape

        for i in range(rows):
            for j in range(cols):
                x = j * self.squareLength
                y = i * self.squareLength
                
                # todo: more generic (without isinstance, working for every chess piece)
                if isinstance(self.matrix[i, j], Pawn):
                    # draw pawn
                    self.matrix[i, j].draw((x+self.xStart+self.squareLength/2,y+self.yStart+self.squareLength/2), self.squareLength/2)

        pygame.display.flip()

    # highlight all moves given
    def highlightMoves(self, moves):
        for move in moves:
            col, row = move
            x = col * self.squareLength
            y = row * self.squareLength
            # draw small circle in field of move
            pygame.draw.circle(self.screen, self.highlightColor, (x+self.xStart+self.squareLength/2,y+self.yStart+self.squareLength/2), self.squareLength / 4)

        pygame.display.flip()
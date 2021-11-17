import numpy as np
import pygame
from Pieces.Bishop import Bishop
from Pieces.ChessPiece import ChessPiece
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook

class Board:
    """ Board is the chess board containing all the chess pieces """
    def __init__(self, numRows, numCols, squareLength, squareColor, screen):
        self.matrix = np.empty((numRows, numCols), dtype="object")
        self.screen = screen
        # side length of the squares
        self.squareLength = squareLength

        # color of non-white squares
        self.squareColor = squareColor
        self.highlightColor = (0, 200, 0)

        # xStart and yStart are used for centering the grid
        width, height = screen.get_size()
        cols, rows = self.matrix.shape
        self.xStart = (width - cols * self.squareLength) / 2
        self.yStart = (height - rows * self.squareLength) / 2


    # if position is in bounds return true, else false
    def inBounds(self, x, y):
        """ check if x and y are valid index values for self.matrix """
        gridWidth, gridHeight = self.matrix.shape
        return (x >= 0 and y >= 0 and x < gridWidth and y < gridHeight)

    # only called once on start of new game
    def initChessPieces(self):
        """ place all chess pieces at their starting positions """
        
        # place all pawns
        width = len(self.matrix[0])
        for col in range(width):
            pawn = Pawn("black", self.matrix, (col, 1), self.screen)
            self.setChessPiece(pawn, col, 1)
        for col in range(width):
            pawn = Pawn("white", self.matrix, (col, 6), self.screen)
            self.setChessPiece(pawn, col, 6)

        # place all rooks
        rook = Rook("black", self.matrix, (0, 0), self.screen)
        self.setChessPiece(rook, 0, 0)
        rook = Rook("black", self.matrix, (7, 0), self.screen)
        self.setChessPiece(rook, 7, 0)

        rook = Rook("white", self.matrix, (0, 7), self.screen)
        self.setChessPiece(rook, 0, 7)
        rook = Rook("white", self.matrix, (7, 7), self.screen)
        self.setChessPiece(rook, 7, 7)

        # place all bishops
        bishop = Bishop("black", self.matrix, (2, 0), self.screen)
        self.setChessPiece(bishop, 2, 0)
        bishop = Bishop("black", self.matrix, (5, 0), self.screen)
        self.setChessPiece(bishop, 5, 0)

        bishop = Bishop("white", self.matrix, (2, 7), self.screen)
        self.setChessPiece(bishop, 2, 7)
        bishop = Bishop("white", self.matrix, (5, 7), self.screen)
        self.setChessPiece(bishop, 5, 7)

        # place all queens
        queen = Queen("black", self.matrix, (3, 0), self.screen)
        self.setChessPiece(queen, 3, 0)
        queen = Queen("white", self.matrix, (4, 7), self.screen)
        self.setChessPiece(queen, 4, 7)

        # place all other chess pieces

    # set specific chess piece to position on board, else return
    def setChessPiece(self, chessPiece, x, y):
        """ set chess piece to specific field """
        if self.inBounds(x, y):
            self.matrix[y, x] = chessPiece

    # return board size
    def getSize(self):
        return self.matrix.shape

    # draw grid using colored squares
    def drawGrid(self):
        """ draw the grid """
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

        pygame.display.flip()

    def drawChessPieces(self):
        """ draw all chess pieces """
        cols, rows = self.matrix.shape

        for i in range(rows):
            for j in range(cols):
                x = j * self.squareLength
                y = i * self.squareLength
                
                if isinstance(self.matrix[i, j], ChessPiece):
                    # draw pawn
                    self.matrix[i, j].draw((x+self.xStart+self.squareLength/2,y+self.yStart+self.squareLength/2), self.squareLength/2)

        pygame.display.flip()

    def highlightMoves(self, moves):
        """ highlight all given moves with small circles """
        for move in moves:
            col, row = move
            x = col * self.squareLength + self.xStart+self.squareLength/2
            y = row * self.squareLength + self.yStart+self.squareLength/2
            # draw small circle in field if moving there is possible
            pygame.draw.circle(self.screen, self.highlightColor, (x,y), self.squareLength / 4)

        pygame.display.flip()
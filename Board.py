import numpy as np
import pygame
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook

class Board:
    """ Board is the chess board containing all the chess pieces """
    def __init__(self, squareLength, squareColor, screen):
        self.grid = np.empty((8, 8), dtype="object") # 8x8 array to store chess pieces
        self.gridColors = []
        self.screen = screen
        # side length of the squares
        self.squareLength = squareLength

        # side length of images
        self.imgSize = (self.squareLength - 5, self.squareLength - 5)

        # color of non-white squares
        self.squareColor = squareColor
        self.highlightColor = (0, 200, 0)

        # xStart and yStart are used for centering the grid
        width, height = screen.get_size()
        cols, rows = self.grid.shape
        self.xStart = (width - cols * self.squareLength) / 2
        self.yStart = (height - rows * self.squareLength) / 2

        self.initChessPieces() # initialize chess pieces


    # if position is in bounds return true, else false
    def inBounds(self, x, y):
        """ check if x and y are valid index values for self.grid """
        gridWidth, gridHeight = self.grid.shape
        return (x >= 0 and y >= 0 and x < gridWidth and y < gridHeight)

    # only called once on start of new game
    def initChessPieces(self):
        """ place all chess pieces at their starting positions """
        self.grid = np.empty((8, 8), dtype="object") # create empty grid

        # create and place all pawns
        pawnImagePath = "Assets/pawn_black.png"
        imageBlack = pygame.image.load(pawnImagePath).convert_alpha()
        pawnImagePath = "Assets/pawn_white.png"
        imageWhite = pygame.image.load(pawnImagePath).convert_alpha()
        width = len(self.grid[0])
        for col in range(width):
            pawn = Pawn("black", self.grid, (col, 1), self.screen, imageBlack)
            self.setChessPiece(pawn, col, 1)
        for col in range(width):
            pawn = Pawn("white", self.grid, (col, 6), self.screen, imageWhite)
            self.setChessPiece(pawn, col, 6)

        # create and place all rooks
        rookImagePath = "Assets/rook_black.png"
        imageBlack = pygame.image.load(rookImagePath).convert_alpha()
        rookImagePath = "Assets/rook_white.png"
        imageWhite = pygame.image.load(rookImagePath).convert_alpha()
        rook = Rook("black", self.grid, (0, 0), self.screen, imageBlack)
        self.setChessPiece(rook, 0, 0)
        rook = Rook("black", self.grid, (7, 0), self.screen, imageBlack)
        self.setChessPiece(rook, 7, 0)

        rook = Rook("white", self.grid, (0, 7), self.screen, imageWhite)
        self.setChessPiece(rook, 0, 7)
        rook = Rook("white", self.grid, (7, 7), self.screen, imageWhite)
        self.setChessPiece(rook, 7, 7)

        # create and place all bishops
        bishopImagePath = "Assets/bishop_black.png"
        imageBlack = pygame.image.load(bishopImagePath).convert_alpha()
        bishopImagePath = "Assets/bishop_white.png"
        imageWhite = pygame.image.load(bishopImagePath).convert_alpha()
        bishop = Bishop("black", self.grid, (2, 0), self.screen, imageBlack)
        self.setChessPiece(bishop, 2, 0)
        bishop = Bishop("black", self.grid, (5, 0), self.screen, imageBlack)
        self.setChessPiece(bishop, 5, 0)

        bishop = Bishop("white", self.grid, (2, 7), self.screen, imageWhite)
        self.setChessPiece(bishop, 2, 7)
        bishop = Bishop("white", self.grid, (5, 7), self.screen, imageWhite)
        self.setChessPiece(bishop, 5, 7)

        # create and place all queens
        queenImagePath = "Assets/queen_black.png"
        imageBlack = pygame.image.load(queenImagePath).convert_alpha()
        queenImagePath = "Assets/queen_white.png"
        imageWhite = pygame.image.load(queenImagePath).convert_alpha()
        queen = Queen("black", self.grid, (3, 0), self.screen, imageBlack)
        self.setChessPiece(queen, 3, 0)
        queen = Queen("white", self.grid, (3, 7), self.screen, imageWhite)
        self.setChessPiece(queen, 3, 7)

        # create and place all knights
        knightImagePath = "Assets/knight_black.png"
        imageBlack = pygame.image.load(knightImagePath).convert_alpha()
        knightImagePath = "Assets/knight_white.png"
        imageWhite = pygame.image.load(knightImagePath).convert_alpha()
        knight = Knight("black", self.grid, (1,0), self.screen, imageBlack)
        self.setChessPiece(knight, 1, 0)
        knight = Knight("black", self.grid, (6,0), self.screen, imageBlack)
        self.setChessPiece(knight, 6, 0)

        knight = Knight("white", self.grid, (1,7), self.screen, imageWhite)
        self.setChessPiece(knight, 1, 7)
        knight = Knight("white", self.grid, (6,7), self.screen, imageWhite)
        self.setChessPiece(knight, 6, 7)

        # place the two kings
        kingImagePath = "Assets/king_black.png"
        imageBlack = pygame.image.load(kingImagePath).convert_alpha()
        imageBlack = pygame.transform.scale(imageBlack, (self.imgSize[0],self.imgSize[1]-10)) # image is too high
        kingImagePath = "Assets/king_white.png"
        imageWhite = pygame.image.load(kingImagePath).convert_alpha()
        imageWhite = pygame.transform.scale(imageWhite, (self.imgSize[0],self.imgSize[1]-10)) # image is too high
        king = King("black", self.grid, (4,0), self.screen, imageBlack)
        self.setChessPiece(king, 4, 0)
        king = King("white", self.grid, (4,7), self.screen, imageWhite)
        self.setChessPiece(king, 4, 7)

    def checkBothKingsAlive(self):
        """ check if both kings are still alive, return boolean + color of dead king """
        cols, rows = self.grid.shape
        whiteKingAlive, blackKingAlive = False, False

        for i in range(rows):
            for j in range(cols):
                if self.grid[i, j] and isinstance(self.grid[i, j], King):
                    if self.grid[i, j].color == "white":
                        whiteKingAlive = True
                    else:
                        blackKingAlive = True

        if whiteKingAlive and blackKingAlive:
            return (True, None)
        elif whiteKingAlive:
            return (False, "black")
        elif blackKingAlive:
            return (False, "white")


    # set specific chess piece to position on board, else return
    def setChessPiece(self, chessPiece, x, y):
        """ set chess piece to specific field """
        if self.inBounds(x, y):
            self.grid[y, x] = chessPiece

    # return board size
    def getSize(self):
        return self.grid.shape

    # draw grid using colored squares
    def drawGrid(self):
        """ draw the grid """
        cols, rows = self.grid.shape

        isWhite = True
        for i in range(rows):
            colorsRow = []
            for j in range(cols):
                x = j * self.squareLength
                y = i * self.squareLength

                square = pygame.Rect(x + self.xStart, y + self.yStart, self.squareLength, self.squareLength)
                if isWhite:
                    pygame.draw.rect(self.screen, (255,255,255), square) # draw white cell
                    colorsRow.append("w")
                else:
                    pygame.draw.rect(self.screen, self.squareColor, square) # draw colored cell
                    colorsRow.append("b")
                
                isWhite = not isWhite # switch black and white
            self.gridColors.append(colorsRow)
            isWhite = not isWhite # after line break: switch again

        # draw square around grid
        square = pygame.Rect(self.xStart, self.yStart, cols * self.squareLength, rows * self.squareLength)
        pygame.draw.rect(self.screen, self.squareColor, square, 2)

        pygame.display.flip()

    def drawChessPieces(self):
        """ draw all chess pieces """
        cols, rows = self.grid.shape

        for i in range(rows):
            for j in range(cols):
                x = j * self.squareLength
                y = i * self.squareLength
                
                if self.grid[i, j] != None:
                    if isinstance(self.grid[i, j], King):
                        offset = 8
                        self.grid[i, j].drawImage((x+self.xStart+self.squareLength/2,y+self.yStart+self.squareLength/2+offset), self.squareLength)
                        continue
                    self.grid[i, j].drawImage((x+self.xStart+self.squareLength/2,y+self.yStart+self.squareLength/2), self.squareLength)
                        

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

    def checkPawnReachedEnd(self):
        """ check if pawns reached other side, return boolean (+ position (x, y) of pawn if true) """
        # check first row for white pawns
        for i in range(len(self.grid[0])):
            cur = self.grid[0][i]
            if cur and cur.color == "white" and isinstance(cur, Pawn):
                #print("found candidate")
                return True, (i, 0)

        # check last row for black pawns
        for i in range(len(self.grid[0])):
            cur = self.grid[len(self.grid)-1][i]
            if cur and cur.color == "black" and isinstance(cur, Pawn):
                #print("found candidate")
                return True, (i, len(self.grid)-1)

        return False, None


    def selectAble(self, color):
        """ get all chess pieces for promotion (all except pawn and king) """

        return ["bishop_"+color, "knight_"+color, "queen_"+color, "rook_"+color]

    def promote(self, pawnPos, pieceNameColor):
        """ promote pawn at pos (x,y) to new chess piece (pieceName = name_color) """

        if None in pawnPos:
            print("pawnPos contains None")
            return

        piece, color = pieceNameColor.split("_")

        newPiece = None
        if piece == "queen": # pawn becomes queen
            queenImagePath = f"Assets/queen_{color}.png"
            image = pygame.image.load(queenImagePath).convert_alpha()
            newPiece = Queen(color, self.grid, pawnPos, self.screen, image)

        elif piece == "knight": # pawn becomes knight
            knightImagePath = f"Assets/knight_{color}.png"
            image = pygame.image.load(knightImagePath).convert_alpha()
            newPiece = Knight(color, self.grid, pawnPos, self.screen, image)

        elif piece == "bishop": # pawn becomes bishop
            bishopImagePath = f"Assets/bishop_{color}.png"
            image = pygame.image.load(bishopImagePath).convert_alpha()
            newPiece = Bishop(color, self.grid, pawnPos, self.screen, image)

        elif piece == "rook": # pawn becomes rook
            rookImagePath = f"Assets/rook_{color}.png"
            image = pygame.image.load(rookImagePath).convert_alpha()
            newPiece = Rook(color, self.grid, pawnPos, self.screen, image)
        
        self.setChessPiece(newPiece, pawnPos[0], pawnPos[1])

        # redraw
        self.screen.fill(pygame.Color("white"))
        self.drawGrid()
        self.drawChessPieces()
import pygame

class ChessPiece:
    """ ChessPiece is the base class for all chess pieces """

    def __init__(self, color, grid, pos, screen, image):
        self.color = color
        self.grid = grid
        self.pos = pos
        self.screen = screen
        self.hasMoved = False

        # load and transform image
        self.image = image
        if self.image:
            self.imageRect = self.image.get_rect()

    # if position is in bounds (in grid) return true, else false
    def inBounds(self, x, y):
        """ check if x and y are valid index values for self.grid """
        gridWidth, gridHeight = self.grid.shape
        return (x >= 0 and y >= 0 and x < gridWidth and y < gridHeight)

    def drawImage(self, drawPos, imageWidth):
        """ draw image of chess piece """
        self.imageRect.x = drawPos[0] - imageWidth / 2
        self.imageRect.y = drawPos[1] - imageWidth / 2

        self.screen.blit(self.image, self.imageRect)

    def moveTo(self, x, y):
        """ move chess piece to new position """
        self.hasMoved = True
        temp_pos = (x, y)
        self.grid[y, x] = self # set to new position
        x,y = self.pos
        self.grid[y, x] = None # clear old position
        self.pos = temp_pos # update own position
import pygame

class ChessPiece:
    """ ChessPiece is the base class for all chess pieces """

    def __init__(self, color, grid, pos, screen):
        self.color = color
        self.grid = grid
        self.pos = pos
        self.screen = screen

    # if position is in bounds (in grid) return true, else false
    def inBounds(self, x, y):
        """ check if x and y are valid index values for self.grid """
        gridWidth, gridHeight = self.grid.shape
        return (x >= 0 and y >= 0 and x < gridWidth and y < gridHeight)

    # for testing: draw circle
    # planned: image of chess piece
    def draw(self, drawPos, radius):
        """ draw chess piece """
        color = self.color
        if self.color == "white":
            color = (200, 200, 200)

        pygame.draw.circle(self.screen, color, drawPos, radius)

    def moveTo(self, x, y):
        """ move chess piece to new position """
        temp_pos = (x, y)
        self.grid[y, x] = self # set to new position
        x,y = self.pos
        self.grid[y, x] = None # clear old position
        self.pos = temp_pos # update own position
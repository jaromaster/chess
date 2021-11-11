import numpy as np

# Pawn is the least powerful chess piece and only worth one point
class Pawn():
    def __init__(self, color, grid, pos=(0,0)):
        self.color = color
        self.grid = grid
        self.pos = pos


    # if position is in bounds (in grid) return true, else false
    def inBounds(self, x, y):
        gridWidth, gridHeight = self.grid.shape

        return (x >= 0 and y >= 0 and x < gridWidth and y < gridHeight)

    # return all moves the pawn could make
    # does not check for other pieces
    def validMoves(self):
        moves = []
        if self.color == "white": # if white (pawn moves from bottom to top)
            x,y = self.pos[0], self.pos[1]
            if self.inBounds(x, y-1): # directly above pawn
                moves.append((x, y-1))
            if self.inBounds(x-1, y-1): # above pawn (left)
                moves.append((x-1,y-1))
            if self.inBounds(x+1, y-1): # above pawn (right)
                moves.append((x+1, y-1))

        else: # if not white (pawn moves from top to bottom)
            x,y = self.pos[0], self.pos[1]
            if self.inBounds(x, y+1): # directly below pawn
                moves.append((x, y+1))
            if self.inBounds(x-1, y+1): # below pawn (left)
                moves.append((x-1,y+1))
            if self.inBounds(x+1, y+1): # below pawn (right)
                moves.append((x+1, y+1))


        return moves

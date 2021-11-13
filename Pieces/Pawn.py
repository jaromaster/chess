import pygame

class Pawn():
    """ Pawn is the least powerful chess piece and only worth one point """
    def __init__(self, color, grid, pos, screen):
        self.color = color
        self.grid = grid
        self.pos = pos
        self.screen = screen

    # if position is in bounds (in grid) return true, else false
    def inBounds(self, x, y):
        gridWidth, gridHeight = self.grid.shape
        return (x >= 0 and y >= 0 and x < gridWidth and y < gridHeight)

    # return all moves the pawn could make
    # checks for friendly chess pieces and enemy chess pieces
    def validMoves(self):
        moves = []
        x,y = self.pos[0], self.pos[1]

        if self.color == "white": # if white (pawn moves from bottom to top)
            # directly above pawn if empty
            if self.inBounds(x, y-1) and self.grid[y-1, x] == None: 
                moves.append((x, y-1))
            # above pawn (left) if not empty and enemy chess piece
            if self.inBounds(x-1, y-1) and self.grid[y-1, x-1] and self.grid[y-1, x-1].color != "white": 
                moves.append((x-1,y-1))
            # above pawn (right) if not empty and enemy chess piece
            if self.inBounds(x+1, y-1) and self.grid[y-1, x+1] and self.grid[y-1, x+1].color != "white": 
                moves.append((x+1, y-1))

        else: # if not white (pawn moves from top to bottom)
            # directly below pawn if empty
            if self.inBounds(x, y+1) and self.grid[y+1, x] == None: 
                moves.append((x, y+1))
            # below pawn (left) if not empty and enemy chess piece
            if self.inBounds(x-1, y+1) and self.grid[y+1, x-1] and self.grid[y+1, x-1].color == "white": 
                moves.append((x-1,y+1))
            # below pawn (right) if not empty and enemy chess piece
            if self.inBounds(x+1, y+1) and self.grid[y+1, x+1] and self.grid[y+1, x+1].color == "white": 
                moves.append((x+1, y+1))

        return moves

    # draw pawn to board
    # for testing: draw circle
    # planned: image of pawn
    def draw(self, drawPos, radius):
        color = self.color
        if self.color == "white":
            color = (200, 200, 200)

        pygame.draw.circle(self.screen, color, drawPos, radius)

from Pieces.ChessPiece import ChessPiece

class Knight(ChessPiece):
    """ The Knight can jump over other chess pieces """
    def __init__(self, color, grid, pos, screen, image):
        super().__init__(color, grid, pos, screen, image)

    def validMoves(self):
        """ validMoves returns an array of all possible moves """
        moves = []

        x, y = self.pos
        if self.inBounds(x+1, y-2):
            if self.grid[y-2, x+1] and self.grid[y-2, x+1].color != self.color or self.grid[y-2, x+1] == None:
                moves.append((x+1, y-2))

        if self.inBounds(x+2, y-1):
            if self.grid[y-1, x+2] and self.grid[y-1, x+2].color != self.color or self.grid[y-1, x+2] == None:
                moves.append((x+2, y-1))

        if self.inBounds(x+2, y+1):
            if self.grid[y+1, x+2] and self.grid[y+1, x+2].color != self.color or self.grid[y+1, x+2] == None:
                moves.append((x+2, y+1))

        if self.inBounds(x+1, y+2):
            if self.grid[y+2, x+1] and self.grid[y+2, x+1].color != self.color or self.grid[y+2, x+1] == None:
                moves.append((x+1, y+2))

        if self.inBounds(x-1, y+2):
            if self.grid[y+2, x-1] and self.grid[y+2, x-1].color != self.color or self.grid[y+2, x-1] == None:
                moves.append((x-1, y+2))

        if self.inBounds(x-2, y+1):
            if self.grid[y+1, x-2] and self.grid[y+1, x-2].color != self.color or self.grid[y+1, x-2] == None:
                moves.append((x-2, y+1))

        if self.inBounds(x-2, y-1):
            if self.grid[y-1, x-2] and self.grid[y-1, x-2].color != self.color or self.grid[y-1, x-2] == None:
                moves.append((x-2, y-1))

        if self.inBounds(x-1, y-2):
            if self.grid[y-2, x-1] and self.grid[y-2, x-1].color != self.color or self.grid[y-2, x-1] == None:
                moves.append((x-1, y-2))
                
        return moves
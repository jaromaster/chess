from Pieces.ChessPiece import ChessPiece

# todo: check if move is possible (checkmate, check), image of king

class King(ChessPiece):
    """ King is the most important chess piece """
    def __init__(self, color, grid, pos, screen, image):
        super().__init__(color, grid, pos, screen, image)

    def validMoves(self):
        """ validMoves returns an array of all possible moves """

        moves = []
        x,y = self.pos[0], self.pos[1]

        # positions above king
        if self.inBounds(x, y-1):
            if self.grid[y-1, x] and self.grid[y-1, x].color != self.color or self.grid[y-1, x] == None:
                moves.append((x, y-1))
        if self.inBounds(x-1, y-1): 
            if self.grid[y-1, x-1] and self.grid[y-1, x-1].color != self.color or self.grid[y-1, x-1] == None:
                moves.append((x-1, y-1))
        if self.inBounds(x+1, y-1): 
            if self.grid[y-1, x+1] and self.grid[y-1, x+1].color != self.color or self.grid[y-1, x+1] == None:
                moves.append((x+1, y-1))
        
        # positions below king
        if self.inBounds(x, y+1): 
            if self.grid[y+1, x] and self.grid[y+1, x].color != self.color or self.grid[y+1, x] == None:
                moves.append((x, y+1))
        if self.inBounds(x-1, y+1):
            if self.grid[y+1, x-1] and self.grid[y+1, x-1].color != self.color or self.grid[y+1, x-1] == None:
                moves.append((x-1, y+1))
        if self.inBounds(x+1, y+1): 
            if self.grid[y+1, x+1] and self.grid[y+1, x+1].color != self.color or self.grid[y+1, x+1] == None:
                moves.append((x+1, y+1))

        # positions next to king
        if self.inBounds(x+1, y): 
            if self.grid[y, x+1] and self.grid[y, x+1].color != self.color or self.grid[y, x+1] == None:
                moves.append((x+1, y))
        if self.inBounds(x-1, y): 
            if self.grid[y, x-1] and self.grid[y, x-1].color != self.color or self.grid[y, x-1] == None:
                moves.append((x-1, y))

        return moves
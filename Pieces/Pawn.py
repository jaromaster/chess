from Pieces.ChessPiece import ChessPiece

class Pawn(ChessPiece):
    """ Pawn is the least powerful chess piece """
    def __init__(self, color, grid, pos, screen):
        super().__init__(color, grid, pos, screen)

    # checks for friendly chess pieces and enemy chess pieces
    def validMoves(self):
        """ validMoves returns an array of all possible moves """
        moves = []
        x,y = self.pos[0], self.pos[1] # x: col, y: row

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
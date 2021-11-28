from Pieces.ChessPiece import ChessPiece

class Pawn(ChessPiece):
    """ Pawn is the least powerful chess piece """
    def __init__(self, color, grid, pos, screen, image):
        super().__init__(color, grid, pos, screen, image)
        self.isFirstMove = True

    # checks for friendly chess pieces and enemy chess pieces
    def validMoves(self):
        """ validMoves returns an array of all possible moves """
        moves = []
        x,y = self.pos[0], self.pos[1] # x: col, y: row

        if self.color == "white": # if white (pawn moves from bottom to top)
            # directly above pawn if empty
            if self.inBounds(x, y-1) and self.grid[y-1, x] == None: 
                moves.append((x, y-1))
            # two steps above (only on first move)
            if self.inBounds(x, y-2) and self.grid[y-2, x] == None and self.isFirstMove: 
                moves.append((x, y-2))
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
            # two steps below (only on first move)
            if self.inBounds(x, y+2) and self.grid[y+2, x] == None and self.isFirstMove: 
                moves.append((x, y+2))
            # below pawn (left) if not empty and enemy chess piece
            if self.inBounds(x-1, y+1) and self.grid[y+1, x-1] and self.grid[y+1, x-1].color == "white": 
                moves.append((x-1,y+1))
            # below pawn (right) if not empty and enemy chess piece
            if self.inBounds(x+1, y+1) and self.grid[y+1, x+1] and self.grid[y+1, x+1].color == "white": 
                moves.append((x+1, y+1))

        return moves
    
    # modify moveTo method from ChessPiece to set isFirstMove
    def moveTo(self, x, y):
        """ move chess piece to new position """
        self.isFirstMove = False
        temp_pos = (x, y)
        self.grid[y, x] = self # set to new position
        x,y = self.pos
        self.grid[y, x] = None # clear old position
        self.pos = temp_pos # update own position
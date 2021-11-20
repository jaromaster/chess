from Pieces.ChessPiece import ChessPiece

class Bishop(ChessPiece):
    """ Bishop can only move diagonally """
    def __init__(self, color, grid, pos, screen, image):
        super().__init__(color, grid, pos, screen, image)

    def validMoves(self):
        """ validMoves returns an array of all possible moves """
        moves = []
        xStart, yStart = self.pos
        x,y = xStart, yStart

        # above left
        x -= 1
        y -= 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece): # if chess piece found
                if self.grid[y, x].color != self.color: # enemy: add to moves
                    moves.append((x,y))

                break

            moves.append((x,y))
            x -= 1
            y -= 1

        # above right
        x = xStart + 1
        y = yStart - 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece):
                if self.grid[y, x].color != self.color:
                    moves.append((x,y))
                
                break

            moves.append((x,y))
            x += 1
            y -= 1

        # below left
        x = xStart - 1
        y = yStart + 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece):
                if self.grid[y, x].color != self.color:
                    moves.append((x,y))
                
                break

            moves.append((x,y))
            x -= 1
            y += 1
        
        # below right
        x = xStart + 1
        y = yStart + 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece):
                if self.grid[y, x].color != self.color:
                    moves.append((x,y))
                
                break

            moves.append((x,y))
            x += 1
            y += 1


        return moves

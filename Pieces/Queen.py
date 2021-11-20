from Pieces.ChessPiece import ChessPiece

class Queen(ChessPiece):
    """ The Queen is the most powerful chess piece """
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

        # get all horizontal moves (right)
        x = xStart
        y = yStart
        x += 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece):
                if self.grid[y, x].color != self.color:
                    moves.append((x, y))
                break

            moves.append((x, y))
            x+=1

        # get all horizontal moves (left)
        x = xStart - 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece): 
                if self.grid[y, x].color != self.color: 
                    moves.append((x, y))
                break

            moves.append((x, y))
            x-=1

        # get all vertical moves (below)
        y += 1
        x = xStart
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece): 
                if self.grid[y, x].color != self.color:
                    moves.append((x, y))
                break

            moves.append((x, y))
            y+=1

        # get all vertical moves (above)
        y = yStart - 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece): 
                if self.grid[y, x].color != self.color:
                    moves.append((x, y))
                break
            
            moves.append((x, y))
            y-=1

        return moves
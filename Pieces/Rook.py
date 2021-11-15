from Pieces.ChessPiece import ChessPiece

class Rook(ChessPiece):
    """ Rook can move horizontally and vertically """
    def __init__(self, color, grid, pos, screen):
        super().__init__(color, grid, pos, screen)

    # checks for friendly chess pieces and enemy chess pieces
    def validMoves(self):
        """ validMoves returns an array of all possible moves """       
        xStart, yStart = self.pos
        x, y = xStart, yStart

        horMoves = []
        vertMoves = []
        # get all horizontal moves (right)
        x += 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece): # if chess piece found
                if self.grid[y, x].color != self.color: # if enemy, add to horMoves
                    horMoves.append((x, y))
                break

            horMoves.append((x, y))
            x+=1
        # get all horizontal moves (left)
        x = xStart - 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece): # if chess piece found
                if self.grid[y, x].color != self.color: # if enemy, add to horMoves
                    horMoves.append((x, y))
                break

            horMoves.append((x, y))
            x-=1

        # get all vertical moves (below)
        y += 1
        x = xStart
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece): # if chess piece found
                if self.grid[y, x].color != self.color: # if enemy, add to vertMoves
                    horMoves.append((x, y))
                break

            horMoves.append((x, y))
            y+=1
        # get all vertical moves (above)
        y = yStart - 1
        while self.inBounds(x, y):
            if isinstance(self.grid[y, x], ChessPiece): # if chess piece found
                if self.grid[y, x].color != self.color: # if enemy, add to vertMoves
                    horMoves.append((x, y))
                break
            
            horMoves.append((x, y))
            y-=1

        return horMoves + vertMoves

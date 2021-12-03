from Pieces.ChessPiece import ChessPiece
from Pieces.Rook import Rook

#todo: check for checks when castling

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


        # castling
        # https://www.chess.com/article/view/how-to-castle-in-chess
        if not self.hasMoved:
            isPossible = True
            if self.color == "white":
                # left
                # check if fields between king and rook are empty
                if not(not self.grid[7, 1] and not self.grid[7, 2] and not self.grid[7, 3]):
                    isPossible = False
                
                # check if rook has not moved
                if not (self.grid[7, 0] and isinstance(self.grid[7, 0], Rook) and not self.grid[7, 0].hasMoved):
                    isPossible = False

                # check if king not in check

                # check if king passes check when castling
                
                if isPossible:
                    moves.append((0, 7))
                isPossible = True

                # right
                # check if fields between king and rook are empty
                if not(not self.grid[7, 5] and not self.grid[7, 6]):
                    isPossible = False

                # check if rook has not moved
                if not (self.grid[7, 7] and isinstance(self.grid[7, 7], Rook) and not self.grid[7, 7].hasMoved):
                    isPossible = False

                # check if king not in check
                # check if king passes check when castling
                if isPossible:
                    moves.append((7, 7))
            else:
                # left
                # check if fields between king and rook are empty
                if not(not self.grid[0, 1] and not self.grid[0, 2] and not self.grid[0, 3]):
                    isPossible = False
                
                # check if rook has not moved
                if not (self.grid[0, 0] and isinstance(self.grid[0, 0], Rook) and not self.grid[0, 0].hasMoved):
                    isPossible = False

                # check if king not in check

                # check if king passes check when castling
                
                if isPossible:
                    moves.append((0, 0))
                isPossible = True

                # right
                # check if fields between king and rook are empty
                if not(not self.grid[0, 5] and not self.grid[0, 6]):
                    isPossible = False

                # check if rook has not moved
                if not (self.grid[0, 7] and isinstance(self.grid[0, 7], Rook) and not self.grid[0, 7].hasMoved):
                    isPossible = False

                # check if king not in check
                # check if king passes check when castling
                if isPossible:
                    moves.append((7, 0))

        return moves


    def moveKing(self, x, y):
        """ move king without checking for castling """
        self.hasMoved = True
        temp_pos = (x, y)
        self.grid[y, x] = self # set to new position
        x,y = self.pos
        self.grid[y, x] = None # clear old position
        self.pos = temp_pos # update own position


    def moveTo(self, x, y):
        """ move king and handle castling """
        if self.grid[y, x] and isinstance(self.grid[y, x], Rook) and self.grid[y, x].color == self.color and not self.hasMoved:
            # castling
            # check if rook is left or right
            if self.grid[y, x].pos[0] == 0: # left
                # move king
                self.moveKing(x+2, y)
                # move rook
                self.grid[y, x].moveTo(self.pos[0]+1, self.pos[1])

            elif self.grid[y, x].pos[0] == 7: # right
                # move king
                self.moveKing(x-1, y)
                # move rook
                self.grid[y, x].moveTo(self.pos[0]-1, self.pos[1])

            return

        # if no castling -> normal movement
        self.moveKing(x, y)
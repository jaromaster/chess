from Pieces.ChessPiece import ChessPiece
from Pieces.Pawn import Pawn
from Pieces.Rook import Rook

#todo: check for checks when castling
class King(ChessPiece):
    """ King is the most important chess piece """
    def __init__(self, color, grid, pos, screen, image):
        super().__init__(color, grid, pos, screen, image)

    def checkPosUnderAttack(self, x, y, color):
        """ check if given position can be attacked by chess pieces """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i, j] and self.grid[i, j].color == color:
                    if isinstance(self.grid[i, j], Pawn) or isinstance(self.grid[i, j], King): # if pawn, not all moves are attacks (directly moving forward), if king, castling is no attack
                        if (x,y) in self.grid[i, j].attackMoves():
                            return True

                    
                    elif (x,y) in self.grid[i, j].validMoves():
                        return True

        return False

    def attackMoves(self):
        """ all moves that can be used for attacking chess pieces """
        moves = []
        x,y = self.pos[0], self.pos[1] # x: col, y: row

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

    def validMoves(self):
        """ validMoves returns an array of all possible moves """
        moves = []
        moves = self.attackMoves()

        # castling
        # https://www.chess.com/article/view/how-to-castle-in-chess
        
        # check if king not in check
        enemyColor = "white" if self.color == "black" else "black"
        if self.checkPosUnderAttack(self.pos[0], self.pos[1], enemyColor):
            return moves

        if self.hasMoved:
            return moves

        castlingPossible = True
        if self.color == "white":
            # left
            # check if all fields between king and rook are empty
            if self.grid[7, 1] or self.grid[7, 2] or self.grid[7, 3]:
                castlingPossible = False 
            # check if king passes check when castling
            elif self.checkPosUnderAttack(1, 7, enemyColor) or self.checkPosUnderAttack(2, 7, enemyColor) or self.checkPosUnderAttack(3, 7, enemyColor):
                castlingPossible = False 
            # check if rook has moved
            elif not self.grid[7, 0] or not isinstance(self.grid[7, 0], Rook) or self.grid[7, 0].hasMoved:
                castlingPossible = False 
            
            if castlingPossible:
                moves.append((0, 7)) # if none of above is true, castling is valid
            castlingPossible = True      
            # right
            # check if all fields between king and rook are empty
            if self.grid[7, 5] or self.grid[7, 6]:
                castlingPossible = False 
            # check if king passes check when castling
            elif self.checkPosUnderAttack(5, 7, enemyColor) or self.checkPosUnderAttack(6, 7, enemyColor):
                castlingPossible = False 
            # check if rook has moved
            elif not self.grid[7, 7] or not isinstance(self.grid[7, 7], Rook) or self.grid[7, 7].hasMoved:
                castlingPossible = False 

            if castlingPossible:
                moves.append((7, 7))
        else:
            # left
            # check if all fields between king and rook are empty
            if self.grid[0, 1] or self.grid[0, 2] or self.grid[0, 3]:
                castlingPossible = False 
            # check if king passes check when castling
            if self.checkPosUnderAttack(1, 0, enemyColor) or self.checkPosUnderAttack(2, 0, enemyColor) or self.checkPosUnderAttack(3, 0, enemyColor):
                castlingPossible = False 
            # check if rook has moved
            if not self.grid[0, 0] or not isinstance(self.grid[0, 0], Rook) or self.grid[0, 0].hasMoved:
                castlingPossible = False 
            
            if castlingPossible:
                moves.append((0, 0)) # if none of above is true, castling is valid
            castlingPossible = True
            # right
            # check if all fields between king and rook are empty
            if self.grid[0, 5] or self.grid[0, 6]:
                castlingPossible = False 
            # check if king passes check when castling
            if self.checkPosUnderAttack(5, 0, enemyColor) or self.checkPosUnderAttack(6, 0, enemyColor):
                castlingPossible = False 
            # check if rook has moved
            if not self.grid[0, 7] or not isinstance(self.grid[0, 7], Rook) or self.grid[0, 7].hasMoved:
                castlingPossible = False 

            if castlingPossible:
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
        """ move king (and handle castling) """
        # castling
        if self.grid[y, x] and isinstance(self.grid[y, x], Rook) and self.grid[y, x].color == self.color and not self.hasMoved:
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
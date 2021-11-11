import numpy as np


class Board:
    def __init__(self, numRows, numCols):
        self.matrix = np.empty((numRows, numCols), dtype="object")

    # set specific chess piece to position on board, else return
    def setChessPiece(self, chessPiece, row, col):
        if (row < len(self.matrix) and col < len(self.matrix[0]) and row >= 0 and col >= 0):
            self.matrix[row, col] = chessPiece

    # return board size
    def getSize(self):
        return self.matrix.shape
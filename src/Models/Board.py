from colorama import Fore

class Board:
    rowLength = 0
    columnLength = 0
    BOARD_STARTING_INDEX = 0

    def __init__(self, rowLength, columnLength):
        self.board = [[0] * columnLength for row in range(rowLength)]
        self.rowLength = rowLength
        self.columnLength = columnLength

    def printBoard(self):
        for rowIndex in range(self.rowLength):
            for columnIndex in range(self.columnLength):
                if self.board[rowIndex][columnIndex] == 0:
                    print(Fore.WHITE+"[+]", end="")
                else:
                    print(Fore.RED+"[+]",end="")

            print()

    def isValidIndex(self,neighbourRowIndex,neighbourColumnIndex):
        if self.BOARD_STARTING_INDEX <= neighbourRowIndex < self.rowLength and self.BOARD_STARTING_INDEX <= neighbourColumnIndex < self.columnLength:
            return True

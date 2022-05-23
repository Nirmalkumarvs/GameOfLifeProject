class Board:
    rowLength = 0
    columnLength = 0
    BOARD_STARTING_INDEX = 0

    def __init__(self, rowLength, columnLength):
        self.board = [[0] * columnLength for row in range(rowLength)]
        self.rowLength = rowLength
        self.columnLength = columnLength
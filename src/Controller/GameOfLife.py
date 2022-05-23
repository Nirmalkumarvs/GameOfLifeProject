class GameOfLife:
    DIRECTIONS = [[-1, -1], [-1, 0], [0, -1], [1, 0], [0, 1], [1, 1], [1, -1], [-1, 1]] #to access the all eight neighbouring cells
    ACTIVE_CELL = 1
    DEAD_CELL = 0

    def isActiveCell(self,Board,rowIndex,columnIndex):
        return Board.board[rowIndex][columnIndex]==self.ACTIVE_CELL

    def makeItASActiveCell(self,resultBoard,rowIndex,columnIndex):
        resultBoard[rowIndex][columnIndex]=self.ACTIVE_CELL

    def makeItAsDeadCell(self,resultBoard,rowIndex,columnIndex):
        resultBoard[rowIndex][columnIndex]=self.DEAD_CELL

    def getActiveNeighbourCellsCount(self,rowIndex,columnIndex,Board):
        activeNeighbourCellsCount=0
        for rowChangeValue, columnChangeValue in self.DIRECTIONS:
            neighbourRowIndex = rowIndex + rowChangeValue
            neighbourColumnIndex = columnIndex + columnChangeValue
            if Board.isValidIndex(neighbourRowIndex, neighbourColumnIndex) and self.isActiveCell(Board,neighbourRowIndex, neighbourColumnIndex):
                activeNeighbourCellsCount += 1
        return activeNeighbourCellsCount
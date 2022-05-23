from src.Models.Boards import *

class GameOfLife:
    DIRECTIONS = [[-1, -1], [-1, 0], [0, -1], [1, 0], [0, 1], [1, 1], [1, -1], [-1, 1]] #to access the all eight neighbouring cells
    ACTIVE_CELL = 1
    DEAD_CELL = 0

    def chooseBoard(self,Board):
        print("Select Board\nAvailable Boards")
        for index,board in enumerate(AVAILABLE_BOARDS):
            print(str(index+1)+")."+board)
        boardChoice=int(input())
        if boardChoice==1:
            setKickbackPattern(Board)
        elif boardChoice==2:
            setTwoGliderPattern(Board)
        elif boardChoice == 3:
            setAcorn(Board)
        elif boardChoice==4:
            setTpattern(Board)
        elif boardChoice == 5:
            setSquarePattern(Board)
        elif boardChoice==6:
            setTrianglePattern(Board)

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

    def playTheGame(self,Board):
        resultBoard=[[0]*Board.columnLength for rowIndex in range(Board.rowLength)]
        for rowIndex in range(Board.rowLength):
            for columnIndex in range(Board.columnLength):
                activeNeighbourCellsCount=self.getActiveNeighbourCellsCount(rowIndex,columnIndex,Board)
                if self.isActiveCell(Board,rowIndex,columnIndex):
                    if activeNeighbourCellsCount < 2 or activeNeighbourCellsCount > 3:
                        self.makeItAsDeadCell(resultBoard,rowIndex,columnIndex)
                    else:
                        self.makeItASActiveCell(resultBoard, rowIndex, columnIndex)
                else:
                    if activeNeighbourCellsCount == 3:
                        self.makeItASActiveCell(resultBoard, rowIndex, columnIndex)
                    else:
                        self.makeItAsDeadCell(resultBoard,rowIndex,columnIndex)
        Board.board[::] = resultBoard[::]
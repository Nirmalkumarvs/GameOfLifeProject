# Python code to demonstrate working of unittest
import unittest
from src.Models.Board import Board
from src.Controller.GameOfLife import GameOfLife
class TestMethods(unittest.TestCase):

    def test_Board(self):
        self.assertEqual([[0]*50 for i in range(10)],Board(10,50).board)

    def test_makeItASActiveCell_method(self):
        boardObj1=Board(10,50)
        boardObj2=Board(10,50)
        gameOfLifeObj=GameOfLife()
        for i in range(5):
            boardObj1.board[i][i]=1
            gameOfLifeObj.makeItASActiveCell(boardObj2.board,i,i)

        self.assertEqual(boardObj2.board,boardObj1.board)

    def test_makeItAsDeadCell_method(self):
        boardObj1 = Board(10, 50)
        boardObj2 = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        for i in range(5):
            boardObj1.board[i][i] = 1
            gameOfLifeObj.makeItAsDeadCell(boardObj2.board, i, i)

        self.assertEqual(boardObj2.board, boardObj1.board)

    def test_makeItAsDeadCell_method(self):
        boardObj = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj.board,0,0)
        self.assertEqual(True, gameOfLifeObj.isActiveCell(boardObj.board,0,0))

    def test_getActiveNeighbourCellsCount_method(self):
        boardObj = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 0, 0)
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 0, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 0, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 1, 0)
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 1, 2)
        self.assertEqual(5, gameOfLifeObj.getActiveNeighbourCellsCount(1,1,boardObj))

    def test_CellWithOneOrNoNeighbors(self):
        boardObj1 = Board(10, 50)
        boardObj2 = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 0, 0)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 1)
        gameOfLifeObj.playTheGame(boardObj2)
        self.assertEqual(boardObj1.board, boardObj2.board)

    def test_CellWithFourOrMoreNeighbors(self):
        boardObj1 = Board(10, 50)
        boardObj2 = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj1.board,0,0)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board,0,2)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board,1,0)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board,1,1)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board,2,1)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board,2,2)

        gameOfLifeObj.makeItASActiveCell(boardObj2.board,0,0)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board,1,0)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board,2,0)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board,2,1)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board,2,2)

        gameOfLifeObj.playTheGame(boardObj1)

        self.assertEqual(boardObj1.board, boardObj2.board)


if __name__ == '__main__':
    unittest.main()

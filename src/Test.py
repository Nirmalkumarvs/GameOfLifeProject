# Python code to demonstrate working of unittest
import unittest
from src.Models.Board import Board
from src.Controller.GameOfLife import GameOfLife

class TestBoard(unittest.TestCase):

    def test_Board(self):
        self.assertEqual([[0]*50 for i in range(10)],Board(10,50).board)

class TestGameOfLifeClassMethods(unittest.TestCase):

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
            gameOfLifeObj.makeItASActiveCell(boardObj2.board,i,i)
        for i in range(5):
            gameOfLifeObj.makeItAsDeadCell(boardObj2.board, i, i)

        self.assertEqual(boardObj2.board, boardObj1.board)

    def test_isActiveCell_method(self):
        boardObj = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj.board,0,0)
        self.assertEqual(True, gameOfLifeObj.isActiveCell(boardObj,0,0))

class TestGameOfLifeGameConditions(unittest.TestCase):
    def test_getActiveNeighbourCellsCount_method(self):
        boardObj = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 0, 0)
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 0, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 0, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 1, 0)
        gameOfLifeObj.makeItASActiveCell(boardObj.board, 1, 2)
        self.assertEqual(5, gameOfLifeObj.getActiveNeighbourCellsCount(1,1,boardObj))



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

    def test_CellWithTwoOrThreeNeighbors(self):
        boardObj1 = Board(10, 50)
        boardObj2 = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 0, 0)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 2, 1)

        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 1, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 1, 0)

        gameOfLifeObj.playTheGame(boardObj1)

        self.assertEqual(boardObj1.board, boardObj2.board)

    def test_DeadCellWithThreeNeighbors(self):
        boardObj1 = Board(10, 50)
        boardObj2 = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 0, 0)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 0)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 2, 2)

        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 1, 1)

        gameOfLifeObj.playTheGame(boardObj1)

        self.assertEqual(boardObj1.board, boardObj2.board)

class Test_StillLifesPattern(unittest.TestCase):

    def test_BlockPattern(self):
        boardObj1 = Board(10, 50)
        boardObj2 = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 2, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 2, 2)

        boardObj2.board=boardObj1.board[::]

        for i in range(10):
            gameOfLifeObj.playTheGame(boardObj1)

        self.assertEqual(boardObj1.board, boardObj2.board)


    def test_BeeHivePattern(self):
        boardObj1 = Board(10, 50)
        boardObj2 = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 3)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 2, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 2, 4)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 3, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 3, 3)

        boardObj2.board=boardObj1.board[::]

        for i in range(10):
            gameOfLifeObj.playTheGame(boardObj1)

        self.assertEqual(boardObj1.board, boardObj2.board)


class Test_OscillatoresPattern(unittest.TestCase):
    def test_BlinkerPattern(self):
        boardObj1 = Board(10, 50)
        boardObj2 = Board(10, 50)
        gameOfLifeObj = GameOfLife()
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 1, 3)

        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 1, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 0, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 2, 2)

        for i in range(9):
            gameOfLifeObj.playTheGame(boardObj1)

        self.assertEqual(boardObj1.board, boardObj2.board)

    def test_ToadPattern(self):
        boardObj1 = Board(10, 50)
        boardObj2 = Board(10, 50)
        gameOfLifeObj = GameOfLife()

        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 2, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 2, 3)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 2, 4)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 3, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 3, 2)
        gameOfLifeObj.makeItASActiveCell(boardObj1.board, 3, 3)

        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 1, 3)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 2, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 2, 4)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 3, 1)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 3, 4)
        gameOfLifeObj.makeItASActiveCell(boardObj2.board, 4, 2)

        for i in range(9):
            gameOfLifeObj.playTheGame(boardObj1)

        self.assertEqual(boardObj1.board, boardObj2.board)


if __name__ == '__main__':
    unittest.main()

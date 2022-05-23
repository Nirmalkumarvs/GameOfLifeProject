# Python code to demonstrate working of unittest
import unittest
from Models import Board

class TestMethods(unittest.TestCase):

    def test_Board(self):
        self.assertEqual([[0]*50 for i in range(10)],Board.Board(10,50).board)


if __name__ == '__main__':
    unittest.main()

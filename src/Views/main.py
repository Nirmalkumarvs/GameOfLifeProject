from src.Models.Board import Board
from src.Controller.GameOfLife import GameOfLife

print("Game instructions:\nPress enter to move to next step\nPress q to quit the game\n")
board = Board(15,50) #Initializing board object to create a board with specifies rows and columns
gameOfLife = GameOfLife() #Initializing the Gameoflife object to process the board
gameOfLife.chooseBoard(board) #to choose board from available boards
board.printBoard()
while True:
    gameOfLife.playTheGame(board)
    print()
    board.printBoard()
    choice=input().strip().lower()
    if choice=='q':
        break



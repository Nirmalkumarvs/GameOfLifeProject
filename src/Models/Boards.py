#to create specified active cell pattern in the board
AVAILABLE_BOARDS=["Kickback","TwoGlider","Acorn","T-pattern","Square","Triangle",]

def setKickbackPattern(Board):
    Board.board[10][5] = 1
    Board.board[10][7] = 1
    Board.board[9][6] = 1
    Board.board[9][7] = 1
    Board.board[8][6] = 1

def setTwoGliderPattern(Board):
    Board.board[5][5] = 1
    Board.board[5][7] = 1
    Board.board[6][6] = 1
    Board.board[6][7] = 1
    Board.board[4][7] = 1

    Board.board[8][14] = 1
    Board.board[8][15] = 1
    Board.board[7][16] = 1
    Board.board[9][15] = 1
    Board.board[9][16] = 1

def setAcorn(Board):
    Board.board[7][5] = 1
    Board.board[7][6] = 1
    Board.board[6][8] = 1
    Board.board[7][9] = 1
    Board.board[7][10] = 1
    Board.board[7][11] = 1
    Board.board[5][6] = 1
    Board.board[4][10] = 1

def setTpattern(Board):
    Board.board[5][5] = 1
    Board.board[5][6] = 1
    Board.board[5][7] = 1
    Board.board[6][6] = 1
    Board.board[7][6] = 1


def setSquarePattern(Board):
    Board.board[5][5] = 1
    Board.board[5][6] = 1
    Board.board[5][7] = 1
    Board.board[6][5] = 1
    Board.board[6][7] = 1
    Board.board[7][5] = 1
    Board.board[7][6] = 1
    Board.board[7][7] = 1

def setTrianglePattern(Board):
    Board.board[5][5] = 1
    Board.board[6][4] = 1
    Board.board[6][6] = 1
    Board.board[7][3] = 1
    Board.board[7][4] = 1
    Board.board[7][5] = 1
    Board.board[7][6] = 1
    Board.board[7][7] = 1
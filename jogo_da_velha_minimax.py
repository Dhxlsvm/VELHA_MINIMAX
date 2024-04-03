token = ["X", "O"]


def createBoard():

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    return board


def isBoardFull(board):

    for i in board:
        if " " in i:
            return False
    return True


def printBoard(board):

    for i in board:
        print(" | ".join(i))
        print("-" * 9)


def getMov(msg):
    try:
        n = int(input(msg))
        if (n >= 1 and n <= 3):
            return n - 1
        else:
            print("Numero precisa estar entra 1 e 3")
            return getMov(msg)
    except:
        print("Numero nao valido")
        return getMov(msg)


def checkMov(board, i, j):

    if board[i][j] == " ":
        return True
    else:
        return False


def doMov(board, i, j, player):

    board[i][j] = token[player]


def checkWinner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == " "):
                return False
    return False


def lastPlayer(board):
    if checkWinner(board):
        countMoves = sum(i.count("X") + i.count("O") for i in board)

        if countMoves % 2 == 0:
            return "O"
        else:
            return "X"


def minimax(board, Maximizing):
    if checkWinner(board):
        if Maximizing:
            return {'score': -1}
        else:
            return {'score': 1}
    elif isBoardFull(board):
        return {'score': 0}

    if Maximizing:
        best_score = {'score': -float('inf')}
        symbol = token[0]
    else:
        best_score = {'score': float('inf')}
        symbol = token[1]

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = symbol
                score = minimax(board, not Maximizing)
                board[i][j] = " "
                score['move'] = (i, j)
                if Maximizing and score['score'] > best_score['score']:
                    best_score = score
                if not Maximizing and score['score'] < best_score['score']:
                    best_score = score
    return best_score

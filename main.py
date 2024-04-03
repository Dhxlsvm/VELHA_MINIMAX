from jogo_da_velha_minimax import createBoard, getMov, checkWinner, printBoard, checkMov, doMov, minimax, lastPlayer, isBoardFull


player = 0
board = createBoard()

while True:
    printBoard(board)
    print("===================")
    if player == 0:
        i = getMov("Digite a linha: ")
        j = getMov("Digite a coluna: ")
    else:
        move = minimax(board, False)['move']
        i, j = move

    if checkMov(board, i, j):
        doMov(board, i, j, player)
        player = (player + 1) % 2
    else:
        print("Posição inválida")

    if checkWinner(board) or isBoardFull(board):
        break

winner = lastPlayer(board)

print("===================")
printBoard(board)
if winner and checkWinner(board):
    print("O JOGADOR", winner, "GANHOU!")
elif isBoardFull(board):
    print("EMPATE!")
print("===================")

import pygame

from jogo_da_velha_minimax import createBoard, getMov, checkWinner, printBoard, checkMov, doMov, minimax, lastPlayer, isBoardFull


pygame.font.init()


def draw_board(win, board):
    for i in range(1, 3):
        pygame.draw.line(win, (23, 145, 135), (30, i * 200),
                         (600 - 30, i * 200), 10)
        pygame.draw.line(win, (23, 145, 135), (i * 200, 30),
                         (i * 200, 600 - 30), 10)

    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("montserratalternatessemibold", 125)
            x = j * 200
            y = i * 200
            text = font.render(board[i][j], 1, (0, 0, 0))
            if board[i][j] == "X":
                text = font.render(board[i][j], 1, (66, 66, 66))
            elif board[i][j] == "O":
                text = font.render(board[i][j], 1, (239, 231, 200))

            win.blit(text, ((x + 60), (y + 30)))


def redraw_window(win, board):
    win.fill((28, 170, 156))
    draw_board(win, board)


def main():
    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Jogo Da Velha")

    board = createBoard()

    redraw_window(win, board)
    pygame.display.update()

    player = 0

    while True:
        if (player == 0):
            jogou = False
            while (not jogou):
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        return
                    elif (event.type == pygame.MOUSEBUTTONUP):
                        pos = pygame.mouse.get_pos()
                        i = int(pos[1]/200)
                        j = int(pos[0]/200)
                        jogou = True
        else:
            if not isBoardFull(board):
                move = minimax(board, False)['move']
                i, j = move
            else:
                return 0
        if (checkMov(board, i, j)):
            doMov(board, i, j, player)
            player = (player + 1) % 2
        redraw_window(win, board)
        pygame.display.update()
        if checkWinner(board) or isBoardFull(board):
            winner = lastPlayer(board)
            font = pygame.font.SysFont("montserratalternatessemibold", 35)
            if winner:
                text = font.render(
                    f"O JOGADOR {winner} GANHOU!", True, (255, 255, 255))
            else:
                text = font.render("EMPATE!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(600 // 2, 600 // 2))
            win.blit(text, text_rect)
            pygame.display.update()
            break


main()

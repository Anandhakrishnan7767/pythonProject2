def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")


def check_win(board, player):
    if ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player)):
        return True
    else:
        return False


def tic_tac_toe():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    players = ['X', 'O']
    current_player = players[0]
    while True:
        print_board(board)
        position = int(input("Enter a position to place " + current_player + " (1-9): "))
        if board[position - 1] == ' ':
            board[position - 1] = current_player
        else:
            print("That position is already taken!")
            continue
        if check_win(board, current_player):
            print_board(board)
            print("Player " + current_player + " wins!")
            break
        if ' ' not in board:
            print_board(board)
            print("Tie game!")
            break
        if current_player == players[0]:
            current_player = players[1]
        else:
            current_player = players[0]

tic_tac_toe()

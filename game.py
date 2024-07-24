import board
import sys
import players

move_map = {
    '1': [0, 0],
    '2': [0, 1],
    '3': [0, 2],
    '4': [1, 0],
    '5': [1, 1],
    '6': [1, 2],
    '7': [2, 0],
    '8': [2, 1],
    '9': [2, 2],
}

if __name__ == '__main__':
    print("Hello, Welcome to tic tac toe")

    board = board.Board()
    player = players.MinMaxPlayer()
    board.print_help()
    board.print()
    turn = ['X', 'O']
    turn_number = 0

    won = False
    prompted_already = False
    while not won:
        if not prompted_already:
            print("Your Move 1-9:")
        prompted_already = False

        # read the input
        move = sys.stdin.read(1)[0]

        if move == '?':
            board.print_help()
            continue
        if move == '\n':
            prompted_already = True
            continue
        if move > '9' or move < '1':
            print("Invalid move, try again. Please enter 1-9 for an empty square of '?' for help")
            continue
        row, col = move_map[move]
        if not board.is_move_legal(row, col):
            print("Invalid Move, position occupied, try again")
            continue
        won = board.make_move(row, col, turn[turn_number])
        turn_number += 1
        turn_number %= 2

        board.print()
        if won:
            print("You won!")
            continue
        if len(board.get_legal_moves()) == 0:
            print("You tied")
            won = True

        if not won:
            # let the other team try
            result = player.make_move(board, play_max=True, play_x=False)
            if result[0] != None:
                won = board.make_move(result[0], result[1], turn[turn_number])
                turn_number += 1
                turn_number %= 2
                board.print()
            else:
                print("No move made....ooopsie")

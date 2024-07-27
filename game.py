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

# play a swift round of one player tic tac toe
if __name__ == '__main__':
    # check a few boards
    myBoard = board.Board()
    assert (False == myBoard.make_move(0, 0, 'X'))
    assert (False == myBoard.make_move(0, 1, 'X'))
    assert (True == myBoard.make_move(0, 2, 'X'))

    myBoard = board.Board()
    assert (False == myBoard.make_move(0, 0, 'X'))
    assert (False == myBoard.make_move(1, 0, 'X'))
    assert (True == myBoard.make_move(2, 0, 'X'))

    myBoard = board.Board()
    assert (False == myBoard.make_move(0, 0, 'X'))
    assert (False == myBoard.make_move(1, 1, 'X'))
    assert (True == myBoard.make_move(2, 2, 'X'))

    # will it block a win
    myBoard = board.Board()
    assert (False == myBoard.make_move(0, 0, 'X'))
    assert (False == myBoard.make_move(1, 1, 'O'))
    assert (False == myBoard.make_move(0, 1, 'X'))
    player = players.MinMaxPlayer()
    assert ((0,2,0) == player.make_move(myBoard, 1, False))

    print("Hello, Welcome to tic tac toe")

    myBoard = board.Board()
    player = players.MinMaxPlayer()
    myBoard.print_help()
    myBoard.print()
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
            myBoard.print_help()
            continue
        if move == '\n':
            prompted_already = True
            continue
        if move > '9' or move < '1':
            print("Invalid move, try again. Please enter 1-9 for an empty square of '?' for help")
            continue
        row, col = move_map[move]
        if not myBoard.is_move_legal(row, col):
            print("Invalid Move, position occupied, try again")
            continue
        won = myBoard.make_move(row, col, turn[turn_number])
        turn_number += 1
        turn_number %= 2

        # print out the board and see if it won
        myBoard.print()
        if won:
            print("You won!")
            continue
        if len(myBoard.get_legal_moves()) == 0:
            print("You tied")
            won = True

        if not won:
            # let the other team try
            result = player.make_move(myBoard, play_max=True, play_x=False)
            if result[0] != None:
                won = myBoard.make_move(result[0], result[1], turn[turn_number])
                turn_number += 1
                turn_number %= 2
                myBoard.print()
            else:
                print("No move made....ooopsie. This should not happen.")

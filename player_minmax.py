import board

opponents_letter = {
    'X': 'O',
    'O': 'X'
}


class MinMaxPlayer:
    _letter = None
    _opponents_letter = None

    def __init__(self, letter):
        self._letter = letter
        self._opponents_letter = opponents_letter[letter]

    def make_move(self, board):
        # find the best move from the list of legal moves
        # make that move
        print(f"legal moves available: {board._legal_moves}")
        row, col, score = self.max_moves(board, 0)
        print(f"make move result: {row}, {col}, {score}")
        return (row, col)

    def max_moves(self, board, depth):
        legal_moves = board.get_legal_moves()
        spacing = "        " * depth
        # if the game is over, stop
        if not legal_moves:
            return (None, None, 0)

        result = (None, None, -1)
        # if the game is not over, try each legal move and then try each follow up
        for row, col in legal_moves:
            # if this move wins, stop and return it.
            if board.make_move(row, col, self._letter):
                print(f"{spacing}win {row}, {col}")
                board.undo_move(row, col)
                return (row, col, 1)

            print(f"{spacing}played {row}, {col}")

            # otherwise, check for the other player's move
            min_result = self.min_moves(board, depth + 1)
            if min_result[2] >= result[2]:
                result = min_result
            board.undo_move(row, col)

        return result


    def min_moves(self, board, depth):
        legal_moves = board.get_legal_moves()
        spacing = "        " * depth

        # if the game is over, stop
        if not legal_moves:
            return (None, None, 0)

        result = (None, None, 1)
        # if the game is not over, try each legal move and then try each follow up
        for row, col in legal_moves:
            # if this move wins, stop and return it.
            if board.make_move(row, col, self._letter):
                print(f"{spacing}loss {row}, {col}")
                board.undo_move(row, col)
                return (row, col, -1)
            print(f"{spacing}played {row}, {col}")

            # otherwise, check for the other player's move
            max_result = self.max_moves(board, depth+1)
            if max_result[2] <= result[2]:
                result = max_result
            board.undo_move(row, col)

        return result

import math

# MinMax algorithm to play tic tac toe
class MinMaxPlayer:
    # make a move, specify if we are playing max or min side, and if we are X or O.
    def make_move(self, board, play_max=True, play_x=True):
        result = (None, None, -math.inf)
        if not play_max:
            result = (None, None, math.inf)

        player = 'X'
        if not play_x:
            player = 'O'

        # get legal moves
        legal_moves = board.get_legal_moves()
        if not legal_moves:
            return (None, None, 0)  # it is a tie

        for move in legal_moves:
            won = board.make_move(move[0], move[1], player)
            if won:
                result = (move[0], move[1], 1)
                if not play_max:
                    result = (move[0], move[1], -1)
                board.undo_move(move[0], move[1])
                return result

            # did not win, allow the other side to try making moves
            inner_result = self.make_move(board, not play_max, not play_x)
            if play_max:
                if inner_result[2] > result[2]:
                    result = (move[0], move[1], inner_result[2])
            else:
                if inner_result[2] < result[2]:
                    result = (move[0], move[1], inner_result[2])

            # undo the move
            board.undo_move(move[0], move[1])

        return result

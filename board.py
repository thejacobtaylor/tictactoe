

# Tic Tac Toe Board
class Board:
    _positions = None
    _legal_moves = None

    # contructor
    def __init__(self):
        self._positions = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        self._legal_moves = set()
        for row in range(3):
            for col in range(3):
                self._legal_moves.add((row, col))

    # make a move to row, col, with letter as the player.
    def make_move(self, row, col, letter):
        assert(letter == 'X' or letter == 'O')
        assert(self.is_move_legal(row, col))
        self._positions[row][col] = letter

        self._legal_moves.remove((row, col))

        return self.is_won(letter)

    # undo a move.
    def undo_move(self, row, col):
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            return False
        self._positions[row][col] = ' '
        self._legal_moves.add((row, col))

    # Get the list of current legal moves.
    def get_legal_moves(self):
        moves = []
        for move in self._legal_moves:
            moves.append(move)
        return moves

    # Is the game won by letter?
    def is_won(self, letter):
        assert (letter == 'X' or letter == 'O')
        for index in range(3):
            if self._check_row(index, letter):
                return True
            if self._check_col(index, letter):
                return True
        return self._check_diagonals(letter)

    # Is the move legal?
    def is_move_legal(self, row, col):
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            return False
        result = self._positions[row][col] == ' '
        if not result:
            print(f"We are considering [{row}, {col}], current value is: {self._positions[row][col]}")
        return  self._positions[row][col] == ' '

    # Print the board for the user to see it.
    def print(self):
        print(self._positions[0][0] + '|' + self._positions[0][1] + '|' + self._positions[0][2])
        print('-'*5)
        print(self._positions[1][0] + '|' + self._positions[1][1] + '|' + self._positions[1][2])
        print('-'*5)
        print(self._positions[2][0] + '|' + self._positions[2][1] + '|' + self._positions[2][2])
        print()

    # Print help so people know the numbers to make moves.
    def print_help(self):
        print('1|2|3')
        print('-'*5)
        print('4|5|6')
        print('-'*5)
        print('7|8|9')
        print("enter the position number followed by enter")
        print("")

    # Check if a row is won.
    def _check_row(self, row, letter):
        if self._positions[row] == [letter, letter, letter]:
            return True
        return False

    # Check if a column is won
    def _check_col(self, col, letter):
        for row in range(3):
            if self._positions[row][col] != letter:
                return False
        return True

    # Check the diagonals.
    def _check_diagonals(self, letter):
        # check top left to lower right
        if self._positions[0][0] == letter and self._positions[1][1] == letter and self._positions[2][2] == letter:
            return True

        # check top left to lower right
        if self._positions[2][0] == letter and self._positions[1][1] == letter and self._positions[0][2] == letter:
            return True

        return False


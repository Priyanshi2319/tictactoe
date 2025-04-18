class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.grid:
            print(' | '.join(row))
            print('-' * 5)

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == ' '

    def place_move(self, row, col, symbol):
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or \
               all(self.grid[j][i] == symbol for j in range(3)):
                return True
        if all(self.grid[i][i] == symbol for i in range(3)) or \
           all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)

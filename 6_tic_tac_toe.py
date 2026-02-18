class TicTacToeHeuristic:
    def __init__(self, board, player, opponent):
        self.board = board
        self.player = player
        self.opponent = opponent

    def open_lines(self, symbol):
        lines = []

        # Rows
        lines.extend(self.board)

        # Columns
        for c in range(3):
            lines.append([self.board[r][c] for r in range(3)])

        # Diagonals
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2 - i] for i in range(3)])

        count = 0
        for line in lines:
            if (
                self.opponent not in line
                if symbol == self.player
                else self.player not in line
            ):
                count += 1
        return count

    def heuristic(self):
        return self.open_lines(self.player) - self.open_lines(self.opponent)


# Example
board = [["X", "O", " "], [" ", "X", " "], ["O", " ", " "]]

ttt = TicTacToeHeuristic(board, "X", "O")
print("Heuristic value e(p):", ttt.heuristic())

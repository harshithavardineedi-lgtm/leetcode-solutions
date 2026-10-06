class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        columns = set()
        diagonals1 = set()
        diagonals2 = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                diagonal1 = row - col
                diagonal2 = row + col

                if col in columns or diagonal1 in diagonals1 or diagonal2 in diagonals2:
                    continue

                board[row][col] = "Q"
                columns.add(col)
                diagonals1.add(diagonal1)
                diagonals2.add(diagonal2)

                backtrack(row + 1)

                board[row][col] = "."
                columns.remove(col)
                diagonals1.remove(diagonal1)
                diagonals2.remove(diagonal2)

        backtrack(0)

        return result    
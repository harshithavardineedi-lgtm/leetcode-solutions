class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    empty.append((r, c))
                else:
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[(r // 3) * 3 + c // 3].add(value)

        def solve(index):
            if index == len(empty):
                return True

            # Choose the empty cell with the fewest options
            best = index
            best_options = None

            for i in range(index, len(empty)):
                r, c = empty[i]
                box = (r // 3) * 3 + c // 3

                options = set("123456789") - rows[r] - cols[c] - boxes[box]

                if best_options is None or len(options) < len(best_options):
                    best = i
                    best_options = options

                    if len(options) == 1:
                        break

            empty[index], empty[best] = empty[best], empty[index]

            r, c = empty[index]
            box = (r // 3) * 3 + c // 3

            for digit in best_options:
                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

                if solve(index + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[box].remove(digit)

            empty[index], empty[best] = empty[best], empty[index]

            return False

        solve(0)
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        def dfs(r, c):
            count = 0

            for i in range(max(0, r-1), min(m, r+2)):
                for j in range(max(0, c-1), min(n, c+2)):
                    if board[i][j] == 'M':
                        count += 1

            if count:
                board[r][c] = str(count)
            else:
                board[r][c] = 'B'

                for i in range(max(0, r-1), min(m, r+2)):
                    for j in range(max(0, c-1), min(n, c+2)):
                        if board[i][j] == 'E':
                            dfs(i, j)

        dfs(r, c)
        return board    
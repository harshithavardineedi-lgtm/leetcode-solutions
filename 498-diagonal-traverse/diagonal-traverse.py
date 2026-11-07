class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        for s in range(m + n - 1):
            diagonal = []

            for i in range(m):
                j = s - i
                if 0 <= j < n:
                    diagonal.append(mat[i][j])

            if s % 2 == 0:
                diagonal.reverse()

            result.extend(diagonal)

        return result    
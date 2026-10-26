from typing import List
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        answer = float("-inf")

        # Square up the smaller dimension for efficiency
        if rows > cols:
            matrix = [list(row) for row in zip(*matrix)]
            rows, cols = cols, rows

        for top in range(rows):
            sums = [0] * cols

            for bottom in range(top, rows):
                for c in range(cols):
                    sums[c] += matrix[bottom][c]

                prefix = [0]
                current = 0

                for value in sums:
                    current += value
                    target = current - k
                    i = bisect_left(prefix, target)

                    if i < len(prefix):
                        answer = max(answer, current - prefix[i])

                    insort(prefix, current)

                    if answer == k:
                        return k

        return answer    
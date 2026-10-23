from functools import lru_cache
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @lru_cache(None)
        def solve(expr):
            results = []

            for i, char in enumerate(expr):
                if char in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i + 1:])

                    for a in left:
                        for b in right:
                            if char == "+":
                                results.append(a + b)
                            elif char == "-":
                                results.append(a - b)
                            else:
                                results.append(a * b)

            if not results:
                return [int(expr)]

            return results

        return solve(expression)
    
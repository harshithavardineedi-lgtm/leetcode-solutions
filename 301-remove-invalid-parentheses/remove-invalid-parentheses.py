from collections import deque
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(text):
            balance = 0

            for char in text:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        queue = deque([s])
        visited = {s}

        while queue:
            level_results = []

            for _ in range(len(queue)):
                current = queue.popleft()

                if is_valid(current):
                    level_results.append(current)

                if level_results:
                    continue

                for i, char in enumerate(current):
                    if char not in "()":
                        continue

                    # Avoid removing consecutive identical parentheses.
                    if i > 0 and current[i] == current[i - 1]:
                        continue

                    candidate = current[:i] + current[i + 1:]

                    if candidate not in visited:
                        visited.add(candidate)
                        queue.append(candidate)

            if level_results:
                return level_results

        return [""]
    
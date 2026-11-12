class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        total = sum(machines)
        n = len(machines)

        if total % n != 0:
            return -1

        target = total // n
        balance = 0
        result = 0

        for m in machines:
            diff = m - target
            balance += diff
            result = max(result, diff, abs(balance))

        return result    
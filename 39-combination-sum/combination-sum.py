class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue

                current.append(candidates[i])
                backtrack(i, remaining - candidates[i], current)
                current.pop()

        candidates.sort()
        backtrack(0, target, [])

        return result    
from functools import lru_cache
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def dp(left, right):
            if left > right:
                return 0

            best = 0

            for i in range(left, right + 1):
                coins = (
                    balloons[left - 1]
                    * balloons[i]
                    * balloons[right + 1]
                )

                coins += dp(left, i - 1)
                coins += dp(i + 1, right)

                best = max(best, coins)

            return best

        return dp(1, n)
    
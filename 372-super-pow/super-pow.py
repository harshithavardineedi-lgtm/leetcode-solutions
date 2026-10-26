from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def power(x: int, n: int) -> int:
            result = 1
            x %= MOD

            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                n //= 2

            return result

        result = 1

        for digit in b:
            result = (power(result, 10) * power(a, digit)) % MOD

        return result    
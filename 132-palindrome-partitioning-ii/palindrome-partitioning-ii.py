class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = list(range(n))

        for i in range(n):
            # Odd-length palindromes
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                cuts = 0 if left == 0 else dp[left - 1] + 1
                dp[right] = min(dp[right], cuts)
                left -= 1
                right += 1

            # Even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                cuts = 0 if left == 0 else dp[left - 1] + 1
                dp[right] = min(dp[right], cuts)
                left -= 1
                right += 1

        return dp[-1]
    
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        length = 0
        has_odd = False

        for count in freq.values():
            length += (count // 2) * 2

            if count % 2 == 1:
                has_odd = True

        return length + 1 if has_odd else length    
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []

        def is_palindrome(text):
            return text == text[::-1]

        def backtrack(start):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return result
    
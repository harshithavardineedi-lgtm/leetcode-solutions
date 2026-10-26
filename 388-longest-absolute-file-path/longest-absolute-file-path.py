class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lengths = {0: 0}
        max_length = 0

        for part in input.split('\n'):
            depth = part.count('\t')
            name = part[depth:]

            if '.' in name:
                max_length = max(
                    max_length,
                    lengths[depth] + len(name)
                )
            else:
                lengths[depth + 1] = (
                    lengths[depth] + len(name) + 1
                )

        return max_length    
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            letters = 0

            while j < n and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            gaps = j - i - 1

            if j == n or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - letters
                each_gap = spaces // gaps
                extra = spaces % gaps

                line = ""
                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (each_gap + (1 if k - i < extra else 0))
                line += words[j - 1]

            result.append(line)
            i = j

        return result

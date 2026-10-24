class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]

                if (len(first) > 1 and first[0] == '0'):
                    continue
                if (len(second) > 1 and second[0] == '0'):
                    continue

                a, b = int(first), int(second)
                pos = j

                while pos < n:
                    total = a + b
                    text = str(total)

                    if not num.startswith(text, pos):
                        break

                    pos += len(text)
                    a, b = b, total

                if pos == n:
                    return True

        return False
    
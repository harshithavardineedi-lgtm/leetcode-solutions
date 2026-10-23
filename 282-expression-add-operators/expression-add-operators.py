from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(index, path, value, last):
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for end in range(index, len(num)):
                if end > index and num[index] == '0':
                    break

                text = num[index:end + 1]
                current = int(text)

                if index == 0:
                    backtrack(end + 1, text, current, current)
                else:
                    backtrack(
                        end + 1, path + '+' + text,
                        value + current, current
                    )
                    backtrack(
                        end + 1, path + '-' + text,
                        value - current, -current
                    )
                    backtrack(
                        end + 1, path + '*' + text,
                        value - last + last * current,
                        last * current
                    )

        backtrack(0, "", 0, 0)
        return result
    
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                position = i + j + 1
                total = digit1 * digit2 + result[position]

                result[position] = total % 10
                result[position - 1] += total // 10

        start = 0
        while start < len(result) and result[start] == 0:
            start += 1

        return "".join(str(digit) for digit in result[start:])   
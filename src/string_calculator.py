import re


class StringCalculator:
    def __init__(self):
        self._customer_delimiters = [',']

    def register_delimiter(self, delimiter):
        self._customer_delimiters.append(delimiter)

    def add(self, numbers: str) -> int:
        if numbers:
            return sum(map(int, re.split("|".join(self._customer_delimiters), numbers)))
        return 0

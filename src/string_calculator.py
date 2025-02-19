import re


class StringCalculator:
    def __init__(self):
        self._customer_delimiters = [',']
        self._detect_new_delimiter_pattern = r"^//(.+)\n(.*)"

    def register_delimiter(self, delimiter):
        self._customer_delimiters.append(delimiter)

    def add(self, numbers: str) -> int:
        if numbers:
            new_delimiter = re.match(self._detect_new_delimiter_pattern, numbers)
            if new_delimiter:
                self.register_delimiter(new_delimiter.group(1))
                numbers = new_delimiter.group(2)
            return sum(map(int, re.split("|".join(self._customer_delimiters), numbers)))
        return 0

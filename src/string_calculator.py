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
            number_list = list(map(int, re.split("|".join(self._customer_delimiters), numbers)))
            negatives = [str(x) for x in number_list if x < 0]
            if not negatives:
                return sum(number_list)
            raise ValueError(f"Found negative numbers: {','.join(negatives)}")
        return 0


if __name__ == '__main__':
    numbers = str(input("Provide number string: "))
    string_calculator = StringCalculator()
    print("Sum of numbers is: ", string_calculator.add(numbers))

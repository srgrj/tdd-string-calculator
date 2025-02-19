from src.string_calculator import StringCalculator

string_calculator = StringCalculator()


def test_empty_string():
    assert string_calculator.add("") == 0


def test_single_number():
    assert string_calculator.add('1') == 1


def test_comma_separated_two_numbers():
    assert string_calculator.add('1,2') == 3


def test_multiple_numbers():
    assert string_calculator.add('1,2,3,4,5') == 15


def test_custom_delimiter():
    string_calculator.register_delimiter("\n")
    assert string_calculator.add("1\n2,3") == 6

def test_delimiter_changing_input():
    assert string_calculator.add("//;\n1;2") == 3
# String Calculator

## Description
A simple string calculator that takes a string of comma-separated numbers and returns their sum. It also supports:
- Handling new lines between numbers.
- Custom delimiters.
- Exception handling for negative numbers.

## Implementation Methodology
This will be implemented using TDD Kata - an exercise in coding, refactoring and test-first

## Method Signature
```python
def add(numbers: str) -> int:
```

## Features
### Basic Summation
- Input: `""` → Output: `0`
- Input: `"1"` → Output: `1`
- Input: `"1,5"` → Output: `6`

### Handling Multiple Numbers
The method should handle an arbitrary number of numbers:
- Input: `"1,2,3,4,5"` → Output: `15`

### Handling New Lines as Delimiters
New lines (`\n`) can be used in place of commas:
- Input: `"1\n2,3"` → Output: `6`

### Supporting Custom Delimiters
To define a custom delimiter, use the format:
```
//[delimiter]\n[numbers]
```
For example:
- Input: `"//;\n1;2"` → Output: `3`
- Input: `"//|\n3|4|5"` → Output: `12`

### Handling Negative Numbers
If a negative number is encountered, an exception is thrown:
```
negative numbers not allowed -1
```
If multiple negative numbers are present, all should be listed in the exception message:
```
negative numbers not allowed -1,-3,-7
```

## Usage
Run the function from the Python command line:
```sh
python -c 'from string_calculator import add; print(add("1,2,3"))'
```


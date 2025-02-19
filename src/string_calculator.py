def add(numbers: str) -> int:
    if numbers:
        return sum(map(int, numbers.split(',')))
    return 0

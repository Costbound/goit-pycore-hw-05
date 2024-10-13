import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    regexp = re.compile(r'\d+\.?\d+')
    for match in re.finditer(regexp, text):
        print(match.group())
        yield float(match.group())

def sum_profit(text: str, num_generator: Callable[[str], Generator[float, None, None]]) -> float:
    sum = float(0)
    print(sum)
    for num in num_generator(text):
        sum += num
    return sum


total = sum_profit(
    "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.",
      generator_numbers
)

print(f'Total revenue: {total:.2f}')
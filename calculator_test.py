import pytest
from calculator import *

num1 = 2
num2 = 2


def test_add():
    assert add(num1, num2) == 4, f"ОШИБКА: ===== проверки сложения {num1} и {num2} ====="


def test_subtract():
    assert subtract(num1, num2) == 0, f"ОШИБКА: ===== проверки вычитания {num1} и {num2} ====="


def test_division2():
    if not division(num1, num2):
        print('Деление на 0')
    else:
        assert division(num1, num2) == 1, f"ОШИБКА: ===== проверки деления {num1} и {num2} ====="


def test_multiply():
    assert multiply(num1, num2) == 4, f"ОШИБКА: ====== проверки умножения {num1} и {num2} ======="


def test_square():
    assert square(num1) == 4, f"ОШИБКА: ====== проверки возведения в квадрат {num1} ======"

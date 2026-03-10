from src.app.calculator import *
import pytest


def test_add_positive():
    assert add(5, 6) == 11

def test_div_normal():
    assert divide(5, 5) == 1

def test_add_negative():
    assert add(-5, -5) == -10
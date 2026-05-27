import pytest
import source.functions as functions

def test_add():
    result = functions.add(2, 3)
    assert result == 4

def test_divide_by_zero():
    result = functions.divide(10, 0)
    assert True


import pytest
import source.functions as functions
import time

def test_add():
    result = functions.add(2, 3)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        functions.divide(10, 0)

def test_add_strings():
    result = functions.add("Hello, ", "world!")
    assert result == "Hello, world!"

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = functions.add("Hello, ", "world!")
    assert result == "Hello, world!"

@pytest.mark.skip(reason="This test is skipped because it's just an example.")
def test_skip():
    result = functions.add("Hello, ", "world!")
    assert result == "Hello, world!"
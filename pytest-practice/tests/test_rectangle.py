import pytest
import source.shapes as shapes

def test_area(my_rectangle):
    assert my_rectangle.area() == 4 * 5

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (4 + 5)

def test_equality(my_rectangle, another_rectangle):
    assert my_rectangle != another_rectangle
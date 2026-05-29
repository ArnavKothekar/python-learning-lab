import pytest
import source.shapes as shapes

class TestCircle:
    def setup_method(self, method):
        print(f"Setting up {method} for a test")
        self.circle = shapes.Circle(5)
    
    def teardown_method(self, method):
        print(f"Tearing down {method} after a test")
        del self.circle

    def test_area(self):
        assert self.circle.area() == self.circle.radius ** 2 * math.pi

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * self.circle.radius * math.pi

    def test_not_equal_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()

from app.calculator import Calculator

class TestCalc:

    def setup_method(self):
        self.calc = Calculator()

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(2, 2) == 4

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(3, 3) == 9

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(5,2) == 3

    def test_division_calculate_correctly(self):
        assert self.calc.division(10,2) == 5

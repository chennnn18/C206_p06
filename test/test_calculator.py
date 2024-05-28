from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_substract(self):
        a = 2
        b = 1
        cal = Calculator()

        result = cal.subtract(a,b)

        expected = 1
        assert result == expected 

    def test_multiply(self):
        a = 5
        b = 10
        cal = Calculator()

        result = cal.multiply(a,b)

        expected = 50
        assert result == expected 

    def test_divison(self):
        a = 20 
        b = 10
        cal = Calculator()

        result =  cal.divide(a,b)

        expected = 2
        assert result == expected 

    def test_ZeroDivisionError(self):
        a = 20 
        b = 0 
        cal = Calculator()

        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)
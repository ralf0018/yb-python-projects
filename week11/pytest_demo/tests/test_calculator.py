import pytest

from mypackage.calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(10, 5) == 5

def test_multiply():
    assert Calculator.multiply(3, 4) == 12

def test_divide():
    assert Calculator.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(10, 0)
        
def test_power():
    assert Calculator.power(2, 3) == 8

def test_root():
    assert Calculator.root(8, 3) == 2
    with pytest.raises(ValueError, match="Cannot take even root of a negative number"):
        Calculator.root(-2, 2)

def test_sine():
    assert Calculator.sine(30) == pytest.approx(0.5)
    
def test_cosine():
    assert Calculator.cosine(60) == pytest.approx(0.5)
    
def test_tangent():
    assert Calculator.tangent(45) == pytest.approx(1.0)
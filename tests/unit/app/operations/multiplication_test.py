import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))

from app.operations.multiplication import MultOperation
import pytest

multOperation = MultOperation()

@pytest.mark.parametrize('number1, number2, result',
    [
        (50, 2, 100),       
        (10, 2, 20),
        (50, 3, 150),
        (100, 5, 500),
        (10, 10, 100),
        (20, 1, 20)
    ]                         
)
def test_multiply(number1, number2, result):
    assert multOperation.multiply(number1, number2) == result
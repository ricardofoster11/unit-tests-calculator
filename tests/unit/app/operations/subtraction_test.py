import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))

from app.operations.subtraction import SubOperation
import pytest

subOperation = SubOperation()

@pytest.mark.parametrize('number1, number2, result',
    [
        (3, 2, 1),
        (4, 1, 3),
        (50, 5, 45)
    ]
)
def test_subtract(number1, number2, result):
    assert subOperation.subtract(number1, number2) == result
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))

from app.operations.addition import AddOperation
from faker import Faker

obj_fake = Faker()

def test_sum():
    addOperation = AddOperation()
    
    number1 = obj_fake.random_number()
    number2 = obj_fake.random_number()
    expect = number1 + number2

    result = addOperation.sum(number1, number2)
    
    assert result == expect
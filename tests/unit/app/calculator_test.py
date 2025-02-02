import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from faker import Faker
from app.calculator import Calculator
from tests.unit.app.test.add import AddOperationSpy
from tests.unit.app.test.sub import SubOperationSpy
from tests.unit.app.test.mul import MultOperationSpy

obj_fake = Faker()

def test_add():
    addOperationSpy = AddOperationSpy()
    calculator = Calculator(addOperationSpy, SubOperationSpy(), MultOperationSpy())

    number1 = obj_fake.random_number()
    number2 = obj_fake.random_number()    

    result = calculator.add(number1, number2, True)
    
    # Teste de entrada
    assert addOperationSpy.sum_attribute['number1'] == number1
    assert addOperationSpy.sum_attribute['number2'] == number2

    # Teste de saida
    assert result is not None

def test_add_none():
    addOperationSpy = AddOperationSpy()
    calculator = Calculator(addOperationSpy, SubOperationSpy(), MultOperationSpy())

    number1 = obj_fake.random_number()
    number2 = obj_fake.random_number()    

    result = calculator.add(number1, number2, None)

    # Teste de entrada
    assert addOperationSpy.sum_attribute == {}
    
    # Teste de saida
    assert result is None
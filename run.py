from app.calculator import Calculator
from app.operations.addition import AddOperation
from app.operations.subtraction import SubOperation

calc = Calculator(AddOperation(), SubOperation())
op1 = calc.add(5, 5, True)
op2 = calc.sub(1, 5, True)

print(op1)
print(op2)
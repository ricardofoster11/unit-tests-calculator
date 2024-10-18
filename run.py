from app.calculator import Calculator
from app.operations.addition import AddOperation
from app.operations.subtraction import SubOperation
from app.operations.multiplication import MultOperation

calc = Calculator(AddOperation(), SubOperation(), MultOperation())
op1 = calc.add(5, 5, True)
op2 = calc.sub(1, 5, True)
op3 = calc.mul(50, 2, True)

print(op1)
print(op2)
print(op3)
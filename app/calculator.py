class Calculator:
    def __init__(self, addition, subtraction, multiplication):
        self.addition = addition
        self.subtraction = subtraction
        self.multiplication = multiplication
    
    def add(self, number1, number2, op):
        if op:
            return self.addition.sum(number1, number2)
        return None

    def sub(self, number1, number2, op):
        if op:
            return self.subtraction.subtract(number1, number2)
        return None
    
    def mul(self, number1, number2, op):
        if op:
            return self.multiplication.multiply(number1, number2)
        return None
    

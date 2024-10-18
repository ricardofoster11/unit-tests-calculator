class Calculator:
    def __init__(self, addition, subtraction):
        self.addition = addition
        self.subtraction = subtraction
    
    def add(self, number1, number2, op):
        if op:
            return self.addition.sum(number1, number2)
        return None

    def sub(self, number1, number2, op):
        if op:
            return self.subtraction.subtract(number1, number2)
        return None
    

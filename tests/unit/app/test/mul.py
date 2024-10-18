from faker import Faker

obj_fake = Faker()

class MultOperationSpy:
    def __init__(self):
        self.mul_attribute = {}
    
    def multiply(self, number1, number2):
        self.mul_attribute['number1'] = number1
        self.mul_attribute['number2'] = number2

        return obj_fake.random_number()
from faker import Faker

obj_fake = Faker()

class AddOperationSpy:
    def __init__(self):
        self.sum_attributer = {}
    
    def sum(self, number1, number2):
        self.sum_attributer['number1'] = number1
        self.sum_attributer['number2'] = number2
        
        return obj_fake.random_number()
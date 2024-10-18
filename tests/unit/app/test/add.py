from faker import Faker

obj_fake = Faker()

class AddOperationSpy:
    def __init__(self):
        self.sum_attribute = {}
    
    def sum(self, number1, number2):
        self.sum_attribute['number1'] = number1
        self.sum_attribute['number2'] = number2
        
        return obj_fake.random_number()
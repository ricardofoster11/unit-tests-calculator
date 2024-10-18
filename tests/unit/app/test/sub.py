from faker import Faker

obj_fake = Faker()

class SubOperationSpy:
    def __init__(self):
        self.sub_attribute = {}
    
    def subtract(self, number1, number2):
        self.sub_attribute['number1'] = number1
        self.sub_attribute['number2'] = number2
        
        return obj_fake.random_number()
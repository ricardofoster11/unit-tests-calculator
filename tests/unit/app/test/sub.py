from faker import Faker

obj_fake = Faker()

class SubOperationSpy:
    def __init__(self):
        self.sub_attributer = {}
    
    def subtract(self, number1, number2):
        self.sub_attributer['number1'] = number1
        self.sub_attributer['number2'] = number2
        
        return obj_fake.random_number()
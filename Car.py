from Vehicle import *

class Car(Vehicle):
    def __init__(self, model, type, rent_per_day):
        super().__init__(model, type, rent_per_day)
    
    def display(self, index):
        print(f"{index}. Car Model: {self.model}\tType: {self.type}\tRent per day: PKR{self.rent_per_day}")
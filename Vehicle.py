class Vehicle:
    def __init__(self, model, type, rent_per_day):
        self.model = model
        self.type = type
        self.rent_per_day = rent_per_day
    
    def get_model(self):
        return self.model
    
    def get_type(self):
        return self.type
    
    def get_rent_per_day(self):
        return self.rent_per_day
from CustomerInvoice import *
from Car import *
from TotalBill import *

class CarRentalSystem:
    MAX_VEHICLES = 10
    
    def __init__(self):
        self.vehicles = []
        self.rented_vehicles = []
        self.total_rent = 0
        self.total_bill = TotalBill()
        self.info = CustomerInvoice()
        
        self.vehicles.append(Car("Honda Civic", "Sedan", 500))
        self.vehicles.append(Car("Toyota Corolla", "Sedan", 600))
        self.vehicles.append(Car("Mg Hector     ", "Suv ", 700))
        self.vehicles.append(Car("Land Cruiser", "Suv", 800))
        self.vehicles.append(Car("BMW 3 Series", "Luxury", 900))
        self.vehicles.append(Car("Mercedes-Benz", "Luxury", 1000))
        self.vehicles.append(Car("Tx Parado ", "SUV", 1100))
        self.vehicles.append(Car("Toyota RAV4", "SUV", 1200))
        self.vehicles.append(Car("Audi E tron ", "Electric", 1300))
        self.vehicles.append(Car("Tesla Model S", "Electric", 1400))
    
    def display_available_cars(self):
        print("="*80)
        print("AVAILABLE CARS FOR RENT".center(80))
        print("="*80)
        for i in range(len(self.vehicles)):
            self.vehicles[i].display(i+1)
        print()
    
    def rent_car(self):
        choice = int(input("\nEnter the car number to rent: "))
        
        if 1 <= choice <= len(self.vehicles):
            vehicle = self.vehicles[choice - 1]
            
            if vehicle in self.rented_vehicles:
                print(f"Sorry, the {vehicle.get_model()} is already rented. Choose another car.\n\n")
            else:
                rental_days = int(input("Enter the number of days to rent the car: "))
                
                rent = rental_days * vehicle.get_rent_per_day()

                vehicle.rental_number = choice

                self.total_rent += rent
                self.total_bill.add_rent(rent)
                
                self.rented_vehicles.append(vehicle)
                customer_name = input("\nEnter your name: ")
                contact_number = input("Enter your Contact Number: ")
                cnic = input("Enter your CNIC Number: ")
                
                invoice = CustomerInvoice(customer_name, vehicle, choice, rental_days, rent, contact_number, cnic)
                invoice.display()
        else:
            print("\nInvalid car number. Please try again.\n\n")
    
    def return_car(self):

        if not self.rented_vehicles:
            print("\nNo cars are currently rented.")
            return
    
        print("="*80)
        print("RETURN A RENTED CAR".center(80))
        print("="*80)
        choice = int(input("Enter the car number to return: "))
        
        if 1 <= choice <= len(self.vehicles):
            vehicle = self.vehicles[choice-1]
            if vehicle in self.rented_vehicles:
                self.rented_vehicles.remove(vehicle)
                print(f"You have returned the {vehicle.get_model()}. Thank you!")
            else:
                print("This car is not currently rented.")
        else:
            print("Invalid car number.")
    
    def display_rented_cars(self):
        print("="*80)
        if not self.rented_vehicles:
            print("NO CAR RENTED CURRENTLY".center(80))
            print("="*80)
        else:
            print("RENTED CARS".center(80))
            print("="*80)
            for i in range(len(self.rented_vehicles)):
                self.rented_vehicles[i].display(i+1)
            print()
    
    def display_total_bill(self):
        self.total_bill.display_total()
    
    def display_record(self):
        self.info.read_file()
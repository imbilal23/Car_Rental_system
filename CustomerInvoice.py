class CustomerInvoice:
    def __init__(self, customer_name=None, rented_vehicle=None, car_number=None, 
                 rental_days=None, total_rent=None, contact_number=None, cnic=None):
        self.customer_name = customer_name
        self.rented_vehicle = rented_vehicle
        self.car_number = car_number
        self.rental_days = rental_days
        self.total_rent = total_rent
        self.contact_number = contact_number
        self.cnic = cnic
    
    def display(self):
        print("="*80)
        print("CUSTOMER INVOICE".center(80))
        print("="*80)
        print(f"Customer Name: {self.customer_name}")
        print(f"CNIC Number: {self.cnic}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Car Model: {self.rented_vehicle.get_model()}")
        print(f"Car Number: {self.car_number}")
        print(f"Rental Days: {self.rental_days}")
        print(f"Rent per Day: PKR{self.rented_vehicle.get_rent_per_day()}")
        print(f"Total Rent: PKR{self.total_rent}")
        print("="*80)
    
        try:
            with open("invoice.txt", "w") as file:
            
                file.write(f"Customer Name: {self.customer_name}\n")
                file.write(f"CNIC Number: {self.cnic}\n")
                file.write(f"Contact Number: {self.contact_number}\n")
                file.write(f"Car Model: {self.rented_vehicle.get_model()}\n")
                file.write(f"Car Number: {self.car_number}\n")
                file.write(f"Rental Days: {self.rental_days}\n")
                file.write(f"Rent per Day: PKR{self.rented_vehicle.get_rent_per_day()}\n")
                file.write(f"Total Rent: PKR{self.total_rent}\n\n")
                file.close()
        except IOError:
            print("Error while saving invoice to file")

    def read_file(self):
        try:
            with open("invoice.txt", "r") as file:
               print("="*80)
               print("CUSTOMER RECORD".center(80))
               print("="*80)
               first_line = file.readline()
               if not first_line:
                   print("No records found in file")
                   return
            
               print(first_line, end='')  
               for line in file:  
                   print(line, end='')
               file.close()    
        except IOError:
           print("No customer records file exists yet")        
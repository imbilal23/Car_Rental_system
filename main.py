from OperationManager import CarRentalSystem

def main():
    username = "user123"
    password = "123pass"
    
    print("="*80)
    print("WELCOME TO THE LOGIN".center(80))
    print("="*80)
    
    while True:
        user = input("Enter Your username: ")
        passwd = input("Enter password: ")
        if passwd != password or user != username:
            print("\nINCORRECT PASSWORD OR USER NAME. PLEASE TRY AGAIN.\n")
        else:
            break
    
    rental_system = CarRentalSystem()
    
    while True:
        print("="*80)
        print("CAR RENTAL SYSTEM MENU".center(80))
        print("="*80)
        print("1. Display available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Display rented cars")
        print("5. Display total bill")
        print("6. Display Customer Record")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("\nDISPLAY AVAILABLE CARS\n")
            rental_system.display_available_cars()
        elif choice == 2:
            rental_system.rent_car()
        elif choice == 3:
            rental_system.return_car()
        elif choice == 4:
            rental_system.display_rented_cars()
        elif choice == 5:
            rental_system.display_total_bill()
        elif choice == 6:
            rental_system.display_record()
        elif choice == 7:
            print("\nTHANK YOU FOR USING THE CAR RENTAL SYSTEM!\n")
            break
        else:
            print("\nINVALID CHOICE. PLEASE TRY AGAIN.\n")

if __name__ == "__main__":
    main()
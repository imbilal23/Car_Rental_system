class TotalBill:
    def __init__(self):
        self.total_rent = 0
    
    def add_rent(self, rent):
        self.total_rent += rent
    
    def display_total(self):
        print("="*80)
        print("TOTAL BILL".center(80))
        print("="*80)
        print(f"Total Payment Of  A Day: PKR{self.total_rent}")
        print("="*80)
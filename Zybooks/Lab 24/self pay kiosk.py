SALES_TAX = 0.07

class SelfPayKiosk:

    # Constructor
    def __init__(self):
        # Complete the constructor
        self.num_customers = 0
        self.total_sales = 0
        self.amount_due = 0
        self.checked_out = False

    # Return total daily sales
    def get_total_sales(self):
        # Update the return statment
        return self.total_sales

    # Return current amount due
    def get_amount_due(self):
        # Update the return statment
        return self.amount_due

    # Return number of customers served
    def get_num_customers(self):
        return self.num_customers

    # Scan one item
    def scan_item(self, price):
        if price > 0 and not self.checked_out:
            self.amount_due += price
        elif price < 0:
            None

    # Apply sales tax to current purchases
    def check_out(self):
        if not self.checked_out:
            self.amount_due = self.amount_due + self.amount_due*SALES_TAX
            self.checked_out = True

    # Cancel current purchases
    def cancel_transaction(self):
        # Type your code here and remove the return statement
        if not self.checked_out:
            self.amount_due = 0

    # Reset register for the day
    def reset_kiosk(self):
        # Type your code here and remove the return statement
        self.num_customers = 0
        self.total_sales = 0
        self.amount_due = 0

    # Apply payment to amount due
    def make_payment(self, payment):
        # Type your code here and remove the return statement
        if self.checked_out:
            if payment >= self.amount_due:
                self.total_sales += self.amount_due
                self.num_customers += 1
                self.amount_due = 0
            elif payment > 0:
                self.total_sales += payment
                self.amount_due -= payment
            elif payment < 0:
                None

    # Simulate multiple transactions
    def simulate_sales(self, num_sales, initial_price, incr_price):
        # Type your code here and remove the return statement
        for i in range(num_sales+1):
            self.scan_item(initial_price)
            self.check_out()
            self.make_payment(initial_price + 1)
            initial_price += incr_price
            #self.num_customers += 1

if __name__ == '__main__':
    kiosk = SelfPayKiosk()
    
    # Test basic operations
    kiosk.scan_item(20.49)
    kiosk.check_out()
    kiosk.make_payment(25.20)
    print(f"Number of customers: {kiosk.get_num_customers()}")
    print(f"Amount due: {kiosk.get_amount_due():.2f}")
    print(f"Total Sales: {kiosk.get_total_sales():.2f}")
    
    # Add statements as instance methods are completed to support development mode testing
    
    # Test simulate_sales()
    kiosk.reset_kiosk()
    kiosk.simulate_sales(100, 5, 2.5)
    print(f"Number of customers: {kiosk.get_num_customers()}")
    print(f"Amount due: {kiosk.get_amount_due():.2f}")
    print(f"Total Sales: {kiosk.get_total_sales():.2f}")

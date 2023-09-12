FULL_TANK = 14

class FancyCar:
    def __init__(self, make = "Old Clunker", mpg = 24.0, tank = 14.0, full_tank = 14.0, engine_on = False):
        # Complete the constructor.
        self.make = make
        self.mpg = mpg
        self.odometer = 5
        self.tank = tank
        self.full_tank = full_tank
        self.engine_on = engine_on

    # Return car model
    def get_model(self):
        # Update the return statment.
        
        return self.make

    # Return car odometer
    def check_odometer(self):
        # Update the return statment.
        
        return self.odometer

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.
        
        return self.mpg

    # Return amount of gas in tank
    def check_gas_gauge(self):
        return self.tank

    # Honk horn
    def honk_horn(self):
        print(f"The {self.get_model()} says beep beep!")

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):

        gas_used = miles_to_drive / self.mpg

        if miles_to_drive > 0 and self.engine_on:
            self.tank = self.tank - gas_used
            self.odometer += miles_to_drive
            
            #If more gas than available used, calculate how much distance was actually traveled
            if self.tank < 0:
                gallons_deficit = 0-self.tank
                milage_to_reduce = gallons_deficit * self.mpg
                self.odometer -= milage_to_reduce
                self.tank = 0.0
                self.engine_on = False

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        
        if amount_to_add > 0 and self.engine_on == False:
            self.tank += amount_to_add

            if self.tank > self.full_tank:
                self.tank = self.full_tank
        


    # Set boolean variable to True
    def start_engine(self):
        self.engine_on = True

    # Set boolean variable to False
    def stop_engine(self):
        self.engine_on = False
        

if __name__ == '__main__':
    my_car = FancyCar()

    # Just for initial testing
    print(f"make={my_car.get_model()}")
    print(f"mpg={my_car.get_mpg()}")
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")
    my_car.honk_horn()
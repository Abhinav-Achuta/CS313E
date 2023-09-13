"""
In-Class Activity 1 solution
Class: C S 313E: Elements of Software Engineering

In this program there are multiple classes that fall under either
condiments or beverages. There is also a vending machiine class
which handles these previously mentioned classes and outputs
data based on the users requests.
"""
class Beverage: #Creating parent class for all beverages
    """ This is a class for all beverages """
    def __init__(self, name, base_cost):
        """ Define values required for each beverage """
        self.name = name
        self.base_cost = base_cost
        self.condiments = []
        self.condiment_counts = {}

    def get_price(self):
        """ Gets the price of the beverage and condiments present """
        total_cost = self.base_cost

        for item in self.condiments:
            total_cost += item.get_price()

        return total_cost

    def count_condiments(self):
        """ Counts the number of each condiment in the drink instance """

        for condiment in self.condiments:
            if condiment.name not in self.condiment_counts:
                self.condiment_counts[condiment.name] = 1
            else:
                self.condiment_counts[condiment.name] +=1

        return self.condiment_counts

    def __str__(self):
        """ Print the beverages name and price """
        return f"{self.name}: ${self.get_price():.2f}"

class Coffee(Beverage): #Creating a class of coffee
    """ Create a class for the coffee """
    base_cost = 1.10

    def __init__(self):
        """ Initialize the coffee name and cost """
        super().__init__("Regular Coffee", Coffee.base_cost)

class Espresso(Beverage): #Creating a class of espresso
    """ Create a class for the espresso """
    base_cost = Coffee.base_cost * 1.2

    def __init__(self):
        """ Initialize the espresso name and cost """
        super().__init__("Espresso", Espresso.base_cost)

class Cappuccino(Beverage): #Creating a class of cappuccino
    """ Create a class for the cappuccino """
    base_cost = Espresso.base_cost * 1.5

    def __init__(self):
        """ Initialize the cappuccino name and cost """
        super().__init__("Cappuccino", Cappuccino.base_cost)

class Condiment: #Creating parent class for all condiments
    """ Create a class for all condiments """
    def __init__(self, name, cost):
        """ Name and cost of each condiment """
        self.name = name
        self.cost= cost

    def get_price(self):
        """ Gets the price of each condiment """
        return self.cost

    def __str__(self):
        """ Prints the condiment name and price """
        return f"{self.name}: ${self.cost:.2f}"

class Sugar(Condiment): #Creating class for sugar
    """ Create sugar as condiment """
    def __init__(self):
        super().__init__("Sugar", 0.10)

class Milk(Condiment): #Creating class for milk
    """ Create milk as condiment """
    def __init__(self):
        super().__init__("Milk", 0.15)

class VendingMachine:
    """ Creating the actual vending machine with all necessary functions """
    def __init__(self):
        self.current_drink = None
        self.customer_numbers = 0
        self.milk_set = False

    def request_drink(self):
        """ Function that will ask user for information on what they want forever"""

        while True:
            print("\nVending machine started up and initiated.")
            print("\nHello! This is the fully operating vending machine.")
            print("What would you link to drink today?")
            print(f"1. Coffee: ${Coffee.base_cost:.2f}"
                  f"\n2. Espresso: ${Espresso.base_cost:.2f}"
                  f"\n3. Cappuccino: ${Cappuccino.base_cost:.2f}")

            #Getting the initial drink
            requested_drink = input("Please enter your selection below:\n")
            try:
                requested_drink = int(requested_drink)
            except ValueError:
                requested_drink = input("That wasn't a valid selection, please try again.\n")

            self.current_drink = self.drink_selection(requested_drink)

            #Condiment portion
            condiment_wanted = input("\nWould you like condiments of milk or sugar? y/n\n")
            self.condiment_selection(condiment_wanted)

            self.reset_machine()

    def drink_selection(self, user_input):
        """ Function that will ask for user input until valid selection is entered """

        if user_input == 1:
            drink = Coffee()
        elif user_input == 2:
            drink = Espresso()
        elif user_input == 3:
            drink = Cappuccino()
        else:
            print("\nSorry, that was not a valid selection. Please enter a valid input.")
            print(f"1. Coffee: ${Coffee.base_cost:.2f}"
                  f"\n2. Espresso: ${Espresso.base_cost:.2f}"
                  f"\n3. Cappuccino: ${Cappuccino.base_cost:.2f}")

            user_input = input("What is your selection?\n")
            try:
                user_input = int(user_input)
            except ValueError:
                user_input = input("What is your selection?\n")
            return self.drink_selection(user_input) #Keep repeating until valid selection is made

        return drink

    def condiment_selection(self, user_input):
        """ Function that will allow users to add condiments to their drink """

        if user_input == "y":
            #Sugar selection
            user_sugar = input(f"\nWould you like sugar(${Sugar().get_price():.2f}ea)? y/n\n")

            while user_sugar not in ("y", "n"): #Repeat if invalid entry
                user_sugar = input("You have made an invalid entry. Please enter y/n:\n")

            if user_sugar == "y":
                self.sugar_selection()


            #Milk selection
            if self.milk_set is False:
                user_milk = input(f"\nWould you like milk(${Milk().get_price():.2f}ea)? y/n\n")

                while user_milk not in ("y", "n"): #Repeat if invalid entry
                    user_milk = input("You have made an invalid entry. Please enter y/n:\n")

                if user_milk == "y":
                    self.milk_selection()
                elif user_milk == "n":
                    self.dispense()

        elif user_input == "n":
            self.dispense()
        else:
            user_input = input("Sorry, that was not a valid selection. Please enter y/n.\n")
            self.condiment_selection(user_input)

    def sugar_selection(self):
        """ Allows user to input how much sugar they want """

        user_sugar = input("You may choose up to 3 cubes of sugar. "
                           "Please enter below how many you want. (0-3)\n")

        try:
            user_sugar = int(user_sugar)

            if 0 <= user_sugar <= 3: #Letting the user add 0-3 sugar cubes
                for i in range(0, user_sugar):
                    self.current_drink.condiments.append(Sugar())
            else:
                print("You did not enter a proper value. Please try again.")
                self.sugar_selection()

            if len(self.current_drink.condiments) == 3:
                print("You have added the maximum amount of condiments.")
                self.dispense()
            else:
                self.milk_selection()

        except ValueError:
            print("You did not enter a correct value. Please try again.")
            self.sugar_selection()

    def milk_selection(self):
        """ Allows user to input how much milk they want """

        #Check how many condiments are remaining
        remaining_condiments = 3-len(self.current_drink.condiments)

        if remaining_condiments > 0:
            user_milk = input(f"You may choose up to {remaining_condiments} milk. "
                              "Enter below how many you would like:\n")

            try:
                user_milk = int(user_milk)
                print(user_milk)

                while user_milk > remaining_condiments:
                    user_milk = input("You did not enter a valid value. "
                                      f"Please enter a number within {remaining_condiments}\n")

                for i in range(0, user_milk):
                    self.current_drink.condiments.append(Milk())
                self.milk_set = True
                self.dispense()

            except ValueError:
                print("You did not enter a valid value. Please try again.")
                self.milk_selection()

    def dispense(self):
        """ Outputs information for the customer about their purchase """

        self.customer_numbers += 1
        condiment_counts = self.current_drink.count_condiments()

        print("\nThank you very much for your business today!")
        print(f"You were customer #{self.customer_numbers}")
        print("Your order reciept with totals is shown below.")
        print(f"Beverage: {self.current_drink.name}(${self.current_drink.base_cost:.2f})")
        print("Condiments:", end = " ")

        try:
            for condiment, count in condiment_counts.items():
                print(f"{condiment}({count})", end = ", ")
            if condiment_counts == {}:
                raise Exception
        except:
            print("None", end="")

        print(f"\nTotal cost: ${self.current_drink.get_price():.2f}")

    def reset_machine(self):
        """ Resets the vending machine's data so it is ready for the next customer """
        print("\n----------------------------")
        print("|The machine is being reset|")
        print("----------------------------")

        self.current_drink = None
        self.milk_set = False

        print("----------------------------")
        print("|The Machine has been reset|")
        print("----------------------------")

    def full_reset_machine(self):
        """ Fully resets the vending machine including customer numbers  """
        self.reset_machine()
        self.customer_numbers = 0

def main():
    """ Main function that will start the vending machine for the first time """
    test_machine = VendingMachine()
    test_machine.request_drink()

if __name__ == "__main__":
    main()

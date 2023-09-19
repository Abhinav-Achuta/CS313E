
class ItemToPurchase():

    def __init__(self, name = "none", price = 0, quantity = 0, description = "none"):
        self.item_name = str(name)
        self.item_price = int(price)
        self.item_quantity = int(quantity)
        self.item_description = str(description)

    def print_item_cost(self):

        total_cost = self.item_quantity*self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
    
    def return_total(self):

        total_cost = self.item_quantity*self.item_price
        
        return total_cost
    
    def print_item_description(self):

        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart():

    def __init__(self, name = "none", date = "January 1,2016", items = []):

        self.customer_name = name
        self.current_date = date
        self.cart_items = items

    def add_item(self, item):

        self.cart_items.append(item)
    
    def remove_item(self, item):

        item_in_cart = False

        for i in range(len(self.cart_items)-1,-1,-1):
            if self.cart_items[i].item_name == item:
                del self.cart_items[i]
                item_in_cart = True

        if not item_in_cart:
            print("Item not found in cart. Nothing removed.")
        
        item_in_cart = False

    def modify_item(self, item):

        item_in_cart = False

        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                self.cart_items[i].item_quantity = item.item_quantity
                item_in_cart = True
        
        if not item_in_cart:
            print("Item not found in cart. Nothing modified.")
        
        item_in_cart = False

    def get_num_items_in_cart(self):
        
        counter = 0

        for object in self.cart_items:
            counter += object.item_quantity

        return counter

    def get_cost_of_cart(self):

        total = 0
        
        for item in self.cart_items:
            total += item.return_total()
        
        return total
    
    def print_total(self):

        if self.cart_items == []:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("Number of Items: 0")
            print()

            print("SHOPPING CART IS EMPTY")
            print()

            print("Total: $0")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            print()

            for object in self.cart_items:
                object.print_item_cost()
            print()

            print(f"Total: ${self.get_cost_of_cart()}")
        print()
        
    def print_descriptions(self):

        if self.cart_items == []:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print()

            print("Item Descriptions")
            for object in self.cart_items:
                object.print_item_description()
            print()

def print_menu():
    print("MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n")

def execute_menu(user_choice, shopping_cart):

    if user_choice == "q":
        # print()
        None
    elif user_choice == "o":
        print("OUTPUT SHOPPING CART")
        shopping_cart.print_total()
    elif user_choice == "i":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        shopping_cart.print_descriptions()
    elif user_choice == "a":
        print("ADD ITEM TO CART")
        new_item_name = input("Enter the item name:\n")
        new_item_description = input("Enter the item description:\n")
        new_item_price = input("Enter the item price:\n")
        new_item_quantity = input("Enter the item quantity:\n")
        print()

        new_item = ItemToPurchase(new_item_name, new_item_price, new_item_quantity, new_item_description)

        shopping_cart.add_item(new_item)
    elif user_choice == "r":
        print("REMOVE ITEM FROM CART")

        item_to_remove = input("Enter name of item to remove:\n")

        shopping_cart.remove_item(item_to_remove)
        print()

    elif user_choice == "c":
        print("CHANGE ITEM QUANTITY")
        modify_item_name = input("Enter the item name:\n")
        modify_item_quantity = input("Enter the new quantity:\n")

        new_modify_item = ItemToPurchase(modify_item_name, 0, modify_item_quantity, "none")

        shopping_cart.modify_item(new_modify_item)
        print()
    

def main():

    #Take in initial user info
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()

    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()

    shopping_cart = ShoppingCart(customer_name, current_date)

    #Printing menu
    print_menu()
    menu_options = "arcioq"

    #Asking user to choose an option
    user_option = input("Choose an option:")

    while user_option not in menu_options:
        print()
        user_option = input("Choose an option:")

    if user_option == "q": #Just to fit stupid zybooks formatting
        print()

    #Executing the option
    execute_menu(user_option, shopping_cart)

    while user_option != "q":
        print_menu()
        user_option = input("Choose an option:")
        print()
        execute_menu(user_option, shopping_cart)

if __name__ == "__main__":
    main()
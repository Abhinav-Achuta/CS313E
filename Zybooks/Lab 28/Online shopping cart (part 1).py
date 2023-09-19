
class ItemToPurchase():

    def __init__(self, name = "none", price = 0, quantity = 0):
        self.item_name = str(name)
        self.item_price = int(price)
        self.item_quantity = int(quantity)

    def print_item_cost(self):

        total_cost = self.item_quantity*self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
    
    def return_total(self):

        total_cost = self.item_quantity*self.item_price
        
        return total_cost

def total_item_costs(list):

    total = 0

    for item in list:
        total += item.return_total()

    return total


def main():

    items_list = []
    
    print("Item 1")
    item_name = input("Enter the item name:\n")
    item_price = input("Enter the item price:\n")
    item_quantity = input("Enter the item quantity:\n")
    item_1 = ItemToPurchase(item_name, item_price, item_quantity)
    items_list.append(item_1)

    print()

    print("Item 2")
    item_name = input("Enter the item name:\n")
    item_price = input("Enter the item price:\n")
    item_quantity = input("Enter the item quantity:\n")
    item_2 = ItemToPurchase(item_name, item_price, item_quantity)
    items_list.append(item_2)

    items_total = total_item_costs(items_list)
    print()

    print("TOTAL COST")
    item_1.print_item_cost()
    item_2.print_item_cost()
    print()

    print(f"Total: ${items_total}")

if __name__ == "__main__":
    main()
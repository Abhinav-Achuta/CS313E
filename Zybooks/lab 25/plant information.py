class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')

class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')
        print(f'   Annual: { self.is_annual }')
        print(f'   Color of flowers: { self.color_of_flowers }')

# TODO:  Define the print_list() function that prints a list of plant (or flower) objects 
def print_list(list):

    current_plant = 1

    for plant in list:

        print(f"Plant {current_plant} Information:")
        plant.print_info()
        print()

        current_plant += 1


if __name__ == "__main__":

    # TODO: Declare a list called my_garden that can hold object of type plant
    my_garden = []

    user_string = input()
    
    while user_string != '-1':
        # TODO: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, color_of_flowers, is_annual
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        split_list = user_string.split()

        #is a plant
        if split_list[0] == "plant":
            my_garden.append(Plant(split_list[1], split_list[2]))
        elif split_list[0] == "flower":
            my_garden.append(Flower(split_list[1], split_list[2], split_list[3], split_list[4]))

        user_string = input()

    # TODO: Call the print_list() function to print my_garden
    print_list(my_garden)
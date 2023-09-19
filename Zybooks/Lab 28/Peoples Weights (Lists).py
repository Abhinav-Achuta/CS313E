# FIXME (1): Prompt for four weights. Add all weights to a list. Output list.

# FIXME (2): Output average of weights.

# FIXME (3): Output max weight from list.

# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.

# FIXME (5): Sort the list and output it.

def average(list):

    return sum(list)/len(list)

def weight_conversion(list, selection):

    in_pounds = list[selection-1]
    in_kilos = in_pounds/2.2

    return in_pounds, in_kilos

def main():

    weights_list = []

    for i in range(1,5):
        user_weight = input(f"Enter weight {i}:\n")
        weights_list.append(float(user_weight))

    print(f"Weights: {weights_list}")
    print()

    weight_avg = average(weights_list)
    print(f"Average weight: {weight_avg:.2f}")

    weight_max = max(weights_list)
    print(f"Max weight: {weight_max:.2f}")
    print()

    user_selection = int(input("Enter a list location (1 - 4):\n"))
    weight_lb, weight_kg = weight_conversion(weights_list, user_selection)
    print(f"Weight in pounds: {weight_lb:.2f}")
    print(f"Weight in kilograms: {weight_kg:.2f}")
    print()

    weights_list.sort()
    print(f"Sorted list: {weights_list}")



if __name__ == "__main__":
    main()
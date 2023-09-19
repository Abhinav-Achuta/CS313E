def sort_dict(dictionary):

    keys = list(dictionary.keys())
    keys_sorted = keys.sort()

    sorted_dictionary = {i: dictionary[i] for i in keys}

    return sorted_dictionary

def ask_info():

    player_dict = {}

    for i in range(1,6):

        jersey_number = int(input(f"Enter player {i}'s jersey number:\n"))
        player_rating = int(input(f"Enter player {i}'s rating:\n"))
        print()

        player_dict[jersey_number] = player_rating

    # player_jerseys = list(player_dict.keys())
    # player_jerseys.sort()

    # players_list = {i: player_dict[i] for i in player_jerseys}

    players_list = sort_dict(player_dict)
    
    return players_list

def print_menu():
    print("MENU\n"
          "a - Add player\n"
          "d - Remove player\n"
          "u - Update player rating\n"
          "r - Output players above a rating\n"
          "o - Output roster\n"
          "q - Quit\n")

def add_player(roster):

    new_jersey = int(input("Enter a jersey number:\n"))
    new_rating = int(input("Enter player rating:\n"))
    print()

    roster[new_jersey] = new_rating

    roster = sort_dict(roster)

    return roster

def remove_player(roster):

    want_to_remove = int(input("Enter a jersey number:\n"))
    print()

    del roster[want_to_remove]

    return roster

def update_roster(roster):

    want_to_update = int(input("Enter a jersey number:\n"))
    new_rating = int(input("Enter a new rating for player:\n"))
    print()

    roster[want_to_update] = new_rating

    return roster

def above_roster(roster):

    rating = int(input("Enter a rating:\n"))
    print()

    print(f"ABOVE {rating}")
    for key in roster:
        if roster[key] > rating:
            print(f"Jersey number: {key}, Rating: {roster[key]}")
    
    print()

def output_roster(dictionary):
    print("ROSTER")
    for key in dictionary:
        print(f"Jersey number: {key}, Rating: {dictionary[key]}")
    print()
    
def execute_menu(user_choice, roster):

    roster = roster

    if user_choice == "q":
        return None
    elif user_choice == "a":
        roster = add_player(roster)
        #output_roster(roster)
    elif user_choice == "o":
        output_roster(roster)
    elif user_choice == "d":
        roster = remove_player(roster)
    elif user_choice == "u":
        roster = update_roster(roster)
    elif user_choice == "r":
        roster = above_roster(roster)

    return roster
    

def main():
    roster = ask_info()

    output_roster(roster)

    #Printing menu
    print_menu()
    menu_options = "aduroq"

    #Asking user to choose an option
    user_option = input("Choose an option:")
    print()

    while user_option not in menu_options:
        user_option = input("Choose an option:")
        print()

    #Executing the option
    roster = execute_menu(user_option, roster)

    while user_option != "q":
        print_menu()
        user_option = input("Choose an option:")
        print()
        roster = execute_menu(user_option, roster)

if __name__ == "__main__":
    main()
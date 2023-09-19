def print_menu():
    print("MENU\n"
        "c - Number of non-whitespace characters\n"
        "w - Number of words\n"
        "f - Fix capitalization\n"
        "r - Replace punctuation\n"
        "s - Shorten spaces\n"
        "q - Quit\n")

def get_num_of_non_WS_characters(sample_text):

    character_counter = 0

    for char in sample_text:
        if char != " ":
            character_counter += 1
    
    return character_counter

def get_num_of_words(sample_text):

    num_words = 1
    previous_char = ""

    for char in sample_text:
        if char == " " and previous_char != " ":
            num_words += 1
        
        previous_char = char
    
    return num_words

def fix_capitalization(sample_text):

    counter = 0
    corrected_sample = ""
    previous_character = ""
    capitalize_next = False

    for i, char in enumerate(sample_text):

        char = str(char)

        if char != " ": #Make anything not a space the previous character
            previous_character = char

        if previous_character in ".?!": #If end of sentence, next char needs to be capitalized
            capitalize_next = True

        if i == 0 or (char != " " and capitalize_next == True): #Capitalze 
            if char.islower(): #Only if char is not already capital, make capital
                counter += 1
                char = char.upper()
                capitalize_next = False

        corrected_sample += char

    return corrected_sample, counter

def replace_punctuation(sample_text, exclamation_count, semicolon_count):

    exclamation_count = 0
    semicolon_count = 0

    corrected_sample = ""

    for char in sample_text:
        if char == "!":
            char = "."
            exclamation_count += 1
        elif char == ";":
            char = ","
            semicolon_count += 1
        
        corrected_sample += char

    print("Punctuation replaced")
    print(f"exclamation_count: {exclamation_count}")
    print(f"semicolon_count: {semicolon_count}")
    
    return corrected_sample

def shorten_space(sample_text):

    corrected_sample = ""
    previous_character = ""
    space_counter = 0

    for char in sample_text:

        char = str(char)

        if char != " ":
            if previous_character == " " and space_counter > 1:
                corrected_sample += " "
                space_counter = 0
            elif previous_character == " " and space_counter == 1:
                corrected_sample += " "

            corrected_sample += char

        if char == " ":
            space_counter += 1

        previous_character = char
    
    return corrected_sample

def execute_menu(sample_text, user_choice):

    if user_choice == "q":
        return True
    elif user_choice == "c":
        chars = get_num_of_non_WS_characters(sample_text)
        print(f"Number of non-whitespace characters: {chars}\n")
    elif user_choice == "w":
        words = get_num_of_words(sample_text)
        print(f"Number of words: {words}\n")
    elif user_choice == "f":
        new_string, capital_counter = fix_capitalization(sample_text)

        print(f"Number of letters capitalized: {capital_counter}")
        print(f"Edited text: {new_string}\n")
    elif user_choice == "r":
        replaced_string = replace_punctuation(sample_text, exclamation_count = 0, semicolon_count = 0)
        print(f"Edited text: {replaced_string}\n")
    elif user_choice == "s":
        corrected_string = shorten_space(sample_text)

        print(f"Edited text: {corrected_string}\n")


def main():
    #Taking user's text
    sample_text = input("Enter a sample text:\n")
    print()
    print("You entered: " + sample_text)
    print()

    #Printing menu
    print_menu()
    menu_options = "cwfrsq"

    #Asking user to choose an option
    user_option = input("Choose an option:")
    print()

    while user_option not in menu_options:
        user_option = input("Choose an option:")
        print()

    #Executing the option
    execute_menu(sample_text, user_option)

    while user_option != "q":
        print_menu()
        user_option = input("Choose an option:")
        print()
        execute_menu(sample_text, user_option)
    

if __name__ == '__main__':
    main()

highway_number = int(input())

''' Type your code here. '''
def direction(num):
    if num % 2 == 0:
        return "east/west"
    else:
        return "north/south"
    
def servicing_highway(num):
    servicing_highway = int(str(num)[-2:])
    return servicing_highway


def highway(user_input):

    #highway_direction = direction(user_input)

    if 0 < user_input < 100:
        return f"I-{user_input} is primary, going {direction(user_input)}."
    elif user_input > 100:
        highway = servicing_highway(user_input)
        if highway > 0:
            return f"I-{user_input} is auxiliary, serving I-{highway}, going {direction(highway)}."
        else:
            return str(user_input) + " is not a valid interstate highway number."
    if user_input == 0:
        return "0 is not a valid interstate highway number."

def main():
    print(highway(highway_number))



if __name__ == "__main__":
    main()